#include "VapourSynth4.h"
#include "plugin_version.h" // One version owner; the .rc file includes the same header.

/*
 * Stage B+ scaffold ONLY. Identity passes the input clip's node reference to
 * the output map; it does not decode MPEG-2, deblock frames, or access indexes.
 * Ownership: mapGetNode provides a reference that mapConsumeNode ALWAYS consumes.
 * No CRT allocation crosses the plugin / VapourSynth boundary.
 */
static void VS_CC identity(const VSMap *in, VSMap *out, void *userData,
                           VSCore *core, const VSAPI *vsapi) {
    (void)userData;
    (void)core;
    int error = 0;
    VSNode *node = vsapi->mapGetNode(in, "clip", 0, &error);
    if (error || !node) {
        vsapi->mapSetError(out, "mpeg2Deblock.Identity: missing clip");
        return;
    }
    if (vsapi->mapConsumeNode(out, "clip", node, maReplace)) {
        vsapi->mapSetError(out, "mpeg2Deblock.Identity: output registration failed");
    }
}

// The VERSIONINFO resource and this VapourSynth plugin version share one header.
VS_EXTERNAL_API(void) VapourSynthPluginInit2(VSPlugin *plugin,
                                             const VSPLUGINAPI *vspapi) {
    const int pluginVersion = VS_MAKE_VERSION(MPEG2D_VERSION_MAJOR, MPEG2D_VERSION_MINOR);
    if (!vspapi->configPlugin("com.hydra3333.mpeg2deblock", "mpeg2deblock",
                             "MPEG-2 Deblocking (scaffold)", pluginVersion,
                             VAPOURSYNTH_API_VERSION, 0, plugin)) {
        return;
    }
    (void)vspapi->registerFunction("Identity", "clip:vnode;", "clip:vnode;",
                                  &identity, nullptr, plugin);
}
