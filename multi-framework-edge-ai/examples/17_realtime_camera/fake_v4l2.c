/* A user-space V4L2 simulation, loaded with LD_PRELOAD, for hosts with no camera and where loading the v4l2loopback kernel module
 * is not acceptable. It handles /dev/video0 and the ioctls the app uses, and feeds real digit images as 640x480 YUYV frames at a fixed rate.
 * It exercises the app's capture code (format negotiation, mmap buffers, queue/dequeue). It does not model a real driver's timing or quirks. */
#define _GNU_SOURCE
#include <dlfcn.h>
#include <fcntl.h>
#include <linux/videodev2.h>
#include <stdarg.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/mman.h>
#include <time.h>
#include <unistd.h>
#define W 640
#define H 480
#define LEN (W * H * 2)
static int g_fd = -1, g_nbuf = 0, g_streaming = 0; static uint32_t g_n, g_frame = 0; static float* g_x; static uint8_t* g_y;
static uint8_t* g_map[8]; static int g_next = 0;
static void load_digits(void) {
  const char* p = getenv("FAKE_V4L2_BIN"); FILE* f = p ? fopen(p, "rb") : NULL;
  if (!f) { fprintf(stderr, "fake_v4l2: set FAKE_V4L2_BIN\n"); exit(2); }
  uint32_t h[3]; if (fread(h, 4, 3, f) != 3) exit(2);
  g_n = h[0]; g_x = malloc(g_n * 64 * 4); g_y = malloc(g_n);
  if (fread(g_x, 4, g_n * 64, f) != g_n * 64 || fread(g_y, 1, g_n, f) != g_n) exit(2);
  fclose(f);
}
int open(const char* path, int flags, ...) {
  static int (*real)(const char*, int, ...); if (!real) real = dlsym(RTLD_NEXT, "open");
  if (strcmp(path, "/dev/video0") == 0) { g_fd = memfd_create("fake_v4l2", 0); load_digits(); return g_fd; }
  va_list a; va_start(a, flags); int m = va_arg(a, int); va_end(a); return real(path, flags, m);
}
static void render(uint8_t* out) {
  uint32_t k = g_frame++ % g_n; const int cell = H / 8, x0 = (W - H) / 2;
  memset(out, 128, LEN);
  for (int y = 0; y < H; ++y) for (int x = 0; x < W; ++x) {
    int gx = x - x0, r = y / cell, c = gx / cell; float v = 0.f;
    if (gx >= 0 && c < 8 && r < 8) v = g_x[k * 64 + r * 8 + c];
    out[(y * W + x) * 2] = (uint8_t)((v + 1.f) * 127.5f);
  }
  out[1] = g_y[k];  /* ground truth for --label-in-chroma */
}
int ioctl(int fd, unsigned long req, ...) {
  static int (*real)(int, unsigned long, ...); if (!real) real = dlsym(RTLD_NEXT, "ioctl");
  va_list a; va_start(a, req); void* arg = va_arg(a, void*); va_end(a);
  if (fd != g_fd) return real(fd, req, arg);
  switch (req) {
    case VIDIOC_S_FMT: { struct v4l2_format* f = arg; f->fmt.pix.width = W; f->fmt.pix.height = H; f->fmt.pix.pixelformat = V4L2_PIX_FMT_YUYV; f->fmt.pix.sizeimage = LEN; f->fmt.pix.bytesperline = W * 2; return 0; }
    case VIDIOC_REQBUFS: { struct v4l2_requestbuffers* r = arg; if (r->count > 8) r->count = 8; g_nbuf = r->count; return ftruncate(g_fd, (off_t)g_nbuf * LEN); }
    case VIDIOC_QUERYBUF: { struct v4l2_buffer* b = arg; b->length = LEN; b->m.offset = b->index * LEN; g_map[b->index] = mmap(NULL, LEN, PROT_READ | PROT_WRITE, MAP_SHARED, g_fd, b->m.offset); return 0; }
    case VIDIOC_QBUF: return 0;
    case VIDIOC_STREAMON: g_streaming = 1; return 0;
    case VIDIOC_STREAMOFF: g_streaming = 0; return 0;
    case VIDIOC_DQBUF: { struct v4l2_buffer* b = arg; struct timespec t = {0, 1000000000 / 60}; nanosleep(&t, NULL);
      b->index = g_next; g_next = (g_next + 1) % g_nbuf; render(g_map[b->index]); b->bytesused = LEN; return 0; }
    default: return -1;
  }
}
