#ifndef MPEG2DEBLOCK_PLUGIN_VERSION_H
#define MPEG2DEBLOCK_PLUGIN_VERSION_H

/*
 * ONE version owner for the plugin's API identity and embedded VERSIONINFO.
 * Update ONLY the four numeric fields here when advancing a version.
 * The text value is stringified FROM the four fields; do not duplicate it.
 * 0.1.0.0 is a provisional scaffold version, not a ratified public release.
 * VapourSynth API version is independent and comes from VapourSynth4.h.
 */
#define MPEG2D_VERSION_MAJOR 0
#define MPEG2D_VERSION_MINOR 1
#define MPEG2D_VERSION_PATCH 0
#define MPEG2D_VERSION_BUILD 0
/* String form is COMPUTED from the four numbers above: no duplicate version. */
#define MPEG2D_VERSION_STRINGIFY_IMPL(x) #x
#define MPEG2D_VERSION_STRINGIFY(x) MPEG2D_VERSION_STRINGIFY_IMPL(x)
#define MPEG2D_VERSION_TEXT MPEG2D_VERSION_STRINGIFY(MPEG2D_VERSION_MAJOR) "." MPEG2D_VERSION_STRINGIFY(MPEG2D_VERSION_MINOR) "." MPEG2D_VERSION_STRINGIFY(MPEG2D_VERSION_PATCH) "." MPEG2D_VERSION_STRINGIFY(MPEG2D_VERSION_BUILD)
#define MPEG2D_VERSION_QUAD MPEG2D_VERSION_MAJOR,MPEG2D_VERSION_MINOR,MPEG2D_VERSION_PATCH,MPEG2D_VERSION_BUILD

#endif
