package org.mfea.digits;
import android.content.res.AssetManager;
public final class Digits {
    static { System.loadLibrary("ncnndigits"); }
    public static native boolean load(AssetManager assets);
    public static native int predict(float[] pixels);
}
