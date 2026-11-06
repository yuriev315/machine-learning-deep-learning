// IREE C runtime API: instance -> device -> session -> bytecode module -> call. usage: iree_digits model.vmfb module.main digits_test.bin [route]
#include <cstdio>
#include <iree/runtime/api.h>
#include "digits.h"
#define CHECK(expr) do { iree_status_t s_ = (expr); if (!iree_status_is_ok(s_)) { iree_status_fprint(stderr, s_); iree_status_free(s_); return 1; } } while (0)
int main(int argc, char** argv) try {
  if (argc < 4) { fprintf(stderr, "usage: %s model.vmfb module.fn digits_test.bin [route]\n", argv[0]); return 2; }
  auto test = digits::load(argv[3]);
  iree_runtime_instance_options_t io; iree_runtime_instance_options_initialize(&io);
  iree_runtime_instance_options_use_all_available_drivers(&io);
  iree_runtime_instance_t* inst = nullptr; CHECK(iree_runtime_instance_create(&io, iree_allocator_system(), &inst));
  iree_hal_device_t* dev = nullptr; CHECK(iree_runtime_instance_try_create_default_device(inst, iree_make_cstring_view("local-sync"), &dev));
  iree_runtime_session_options_t so; iree_runtime_session_options_initialize(&so);
  iree_runtime_session_t* sess = nullptr; CHECK(iree_runtime_session_create_with_device(inst, &so, dev, iree_runtime_instance_host_allocator(inst), &sess));
  CHECK(iree_runtime_session_append_bytecode_module_from_file(sess, argv[1]));
  iree_runtime_call_t call; CHECK(iree_runtime_call_initialize_by_name(sess, iree_make_cstring_view(argv[2]), &call));
  const iree_hal_dim_t shape[4] = {1, 8, 8, 1};  // NHWC
  digits::Stats st;
  iree_hal_buffer_params_t bp = {}; bp.type = IREE_HAL_MEMORY_TYPE_DEVICE_LOCAL; bp.access = IREE_HAL_MEMORY_ACCESS_ALL; bp.usage = IREE_HAL_BUFFER_USAGE_DEFAULT;
  for (uint32_t i = 0; i < test.n; ++i) {
    iree_hal_buffer_view_t* in = nullptr;
    CHECK(iree_hal_buffer_view_allocate_buffer_copy(dev, iree_runtime_session_device_allocator(sess), 4, shape, IREE_HAL_ELEMENT_TYPE_FLOAT_32, IREE_HAL_ENCODING_TYPE_DENSE_ROW_MAJOR, bp,
        iree_make_const_byte_span(test.image(i), 64 * sizeof(float)), &in));
    CHECK(iree_runtime_call_inputs_push_back_buffer_view(&call, in));
    iree_hal_buffer_view_release(in);
    auto t0 = digits::Clock::now();
    CHECK(iree_runtime_call_invoke(&call, 0));
    double us = digits::us_since(t0);
    iree_hal_buffer_view_t* out = nullptr; CHECK(iree_runtime_call_outputs_pop_front_buffer_view(&call, &out));
    float logits[10];
    CHECK(iree_hal_device_transfer_d2h(dev, iree_hal_buffer_view_buffer(out), 0, logits, sizeof(logits), IREE_HAL_TRANSFER_BUFFER_FLAG_DEFAULT, iree_infinite_timeout()));
    iree_hal_buffer_view_release(out);
    st.add(us, digits::argmax(logits, 10) == test.labels[i]);
    iree_runtime_call_reset(&call);
  }
  st.report(argc > 4 ? argv[4] : "iree_c_api", argv[1]);
  iree_runtime_call_deinitialize(&call); iree_runtime_session_release(sess); iree_hal_device_release(dev); iree_runtime_instance_release(inst);
  return 0;
} catch (const std::exception& e) { fprintf(stderr, "error: %s\n", e.what()); return 1; }
