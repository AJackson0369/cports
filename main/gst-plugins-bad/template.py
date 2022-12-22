pkgname = "gst-plugins-bad"
pkgver = "1.20.4"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-feature=enabled",
    "-Ddefault_library=shared",
    "-Dglib-asserts=disabled",
    "-Dglib-checks=disabled",
    "-Dgobject-cast-checks=disabled",
    "-Dexamples=disabled",
    "-Ddoc=disabled",
    "-Dhls-crypto=openssl",
    # there are too many auto features and it's difficult to take care that
    # nothing is accidentally disabled and so on, so implicitly enable all,
    # and then disable what's not relevant to us:
    "-Dopencv=disabled",
    "-Dandroidmedia=disabled",
    "-Dapplemedia=disabled",
    "-Dd3dvideosink=disabled",
    "-Dd3d11=disabled",
    "-Ddirectfb=disabled",
    "-Ddirectsound=disabled",
    "-Dfaac=disabled",
    "-Dfbdev=disabled",
    "-Dkate=disabled",
    "-Dmediafoundation=disabled",
    "-Dmsdk=disabled",
    "-Dmusepack=disabled",
    "-Dneon=disabled",
    "-Dnvcodec=disabled",
    "-Donnx=disabled",
    "-Dopenexr=disabled",
    "-Dopenh264=disabled",
    "-Dopenmpt=disabled",
    "-Dopenni2=disabled",
    "-Dopensles=disabled",
    "-Dsctp=disabled",
    "-Dsmoothstreaming=disabled",
    "-Dsrt=disabled",
    "-Dsvthevcenc=disabled",
    "-Dteletext=disabled",
    "-Dtinyalsa=disabled",
    "-Dvoaacenc=disabled",
    "-Dvoamrwbenc=disabled",
    "-Dwasapi=disabled",
    "-Dwasapi2=disabled",
    "-Dwildmidi=disabled",
    "-Dwinks=disabled",
    "-Dwinscreencap=disabled",
    "-Dwpe=disabled",
    "-Dmagicleap=disabled",
    "-Davtp=disabled",
    "-Ddc1394=disabled", # maybe?
    "-Ddts=disabled", # GPL
    "-Dfaad=disabled", # GPL
    "-Dgs=disabled", # does anybody need this?
    "-Diqa=disabled", # AGPL
    "-Dmpeg2enc=disabled", # GPL
    "-Dmplex=disabled", # GPL
    "-Dresindvd=disabled", # GPL
    "-Dx265=disabled", # GPL
    "-Dzbar=disabled", # maybe?
    "-Dzxing=disabled", # maybe?
]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "glib-devel", "orc",
    "gobject-introspection", "shaderc-progs", "wayland-progs",
]
makedepends = [
    "gstreamer-devel", "gst-plugins-base-devel", "openssl-devel",
    "libaom-devel", "libass-devel", "bluez-devel", "libbs2b-devel",
    "libbz2-devel", "pango-devel", "cairo-devel", "lcms2-devel",
    "libcurl-devel", "libssh2-devel", "libxml2-devel", "fdk-aac-devel",
    "fluidsynth-devel", "mesa-devel", "libdrm-devel", "libde265-devel",
    "libmodplug-devel", "openjpeg-devel", "opus-devel", "sbc-devel",
    "librsvg-devel", "librtmp-devel", "libsndfile-devel", "libva-devel",
    "vulkan-loader", "vulkan-headers", "libwebp-devel", "libgudev-devel",
    "wayland-devel", "wayland-protocols", "libxkbcommon-devel",
    "webrtc-audio-processing-devel", "webrtc-audio-processing-0.3-devel",
    "v4l-utils-devel", "libusb-devel", "libfreeaptx-devel", "lilv-devel",
    "ladspa-sdk", "lrdf-devel", "chromaprint-devel", "flite-devel",
    "openal-soft-devel", "qrencode-devel", "json-glib-devel",
    "libnice-devel", "libsrtp-devel", "spandsp-devel", "soundtouch-devel",
    "libmicrodns-devel", "gsm-devel", "libgme-devel", "linux-headers",
]
depends = [f"gst-plugins-base~{pkgver}"]
pkgdesc = "GStreamer bad plugins"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "a1a3f53b3604d9a04fdd0bf9a1a616c3d2dab5320489e9ecee1178e81e33a16a"
# TODO: a few fails, debug later
options = ["!check", "!cross"]

if self.profile().endian == "big":
    configure_args += ["-Dldac=disabled"]
else:
    makedepends += ["ldacbt-devel"]

@subpackage("gst-plugins-bad-devel")
def _devel(self):
    self.depends += [f"gst-plugins-base-devel~{pkgver}"]

    return self.default_devel()

# FIXME visibility
hardening = ["!vis"]
