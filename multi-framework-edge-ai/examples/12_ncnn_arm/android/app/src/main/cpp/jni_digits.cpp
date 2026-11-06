// SDK_REQUIRED: not compiled here, because the NDK is over the 100 MiB download limit. JNI bridge for the ncnn model from Project 12.
#include <android/asset_manager_jni.h>
#include <android/log.h>
#include <jni.h>
#include <net.h>
#include <algorithm>
static ncnn::Net g_net;
extern "C" JNIEXPORT jboolean JNICALL Java_org_mfea_digits_Digits_load(JNIEnv* env, jclass, jobject assets) {
  AAssetManager* mgr = AAssetManager_fromJava(env, assets);
  g_net.opt.num_threads = 2;
  return g_net.load_param(mgr, "tinycnn_opt.param") == 0 && g_net.load_model(mgr, "tinycnn_opt.bin") == 0;
}
extern "C" JNIEXPORT jint JNICALL Java_org_mfea_digits_Digits_predict(JNIEnv* env, jclass, jfloatArray pixels) {
  if (env->GetArrayLength(pixels) != 64) return -1;
  jfloat* p = env->GetFloatArrayElements(pixels, nullptr);
  ncnn::Mat in = ncnn::Mat(8, 8, 1, p, 4u).clone();
  env->ReleaseFloatArrayElements(pixels, p, JNI_ABORT);
  ncnn::Extractor ex = g_net.create_extractor();
  ncnn::Mat out;
  if (ex.input("input", in) != 0 || ex.extract("logits", out) != 0) { __android_log_print(ANDROID_LOG_ERROR, "digits", "inference failed"); return -1; }
  const float* o = out;
  return jint(std::max_element(o, o + out.w) - o);
}
