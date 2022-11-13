pkgname = "mpv"
pkgver = "0.35.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlibmpv=true", "-Dbuild-date=false",
    # most of these are autos, force some we really care about
    "-Dcaca=enabled",
    "-Dcdda=enabled",
    "-Dcplugins=enabled",
    "-Ddrm=enabled",
    "-Degl=enabled",
    "-Ddvbin=enabled",
    "-Ddvdnav=enabled",
    "-Dgl=enabled",
    "-Djack=enabled",
    "-Dlcms2=enabled",
    "-Dlibarchive=enabled",
    "-Dlibbluray=enabled",
    "-Dlibplacebo=enabled",
    "-Dmanpage-build=enabled",
    "-Dpipewire=enabled",
    "-Drubberband=enabled",
    "-Dshaderc=enabled",
    "-Duchardet=enabled",
    "-Dvapoursynth=enabled",
    "-Dvaapi=enabled",
    "-Dvdpau=enabled",
    "-Dvulkan=enabled",
    "-Dwayland=enabled",
    "-Dx11=enabled",
    "-Dxv=enabled",
    "-Dzimg=enabled",
    "-Dzlib=enabled",
    # stuff we don't want
    "-Djavascript=disabled",
    "-Dsdl2=disabled",
    "-Dalsa=disabled",
    "-Dopenal=disabled",
    "-Dopensles=disabled",
    "-Doss-audio=disabled",
    "-Dpulse=disabled",
    "-Dsdl2-audio=disabled",
    # misc
    "-Dlua=lua5.1",
]
hostmakedepends = [
    "meson", "pkgconf", "python-docutils", "wayland-progs"
]
makedepends = [
    "libarchive-devel", "lua5.1-devel", "libuuid-devel", "mesa-devel",
    "vulkan-headers", "vulkan-loader", "libplacebo-devel", "shaderc-devel",
    "ffmpeg-devel", "libxv-devel", "libxrandr-devel", "libxinerama-devel",
    "libxscrnsaver-devel", "libxkbcommon-devel", "libxpresent-devel",
    "wayland-devel", "wayland-protocols", "libvdpau-devel", "libva-devel",
    "pipewire-devel", "pipewire-jack-devel", "lcms2-devel", "libass-devel",
    "libbluray-devel", "libdvdnav-devel", "libcdio-paranoia-devel",
    "rubberband-devel", "uchardet-devel", "harfbuzz-devel", "libcaca-devel",
    "zimg-devel", "vapoursynth-devel",
]
depends = ["hicolor-icon-theme"]
pkgdesc = "Video player based on mplayer2"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://mpv.io"
source = f"https://github.com/mpv-player/{pkgname}/archive/v{pkgver}.tar.gz"
sha256 = "dc411c899a64548250c142bf1fa1aa7528f1b4398a24c86b816093999049ec00"
# development-only
options = ["!check"]

@subpackage("mpv-devel")
def _devel(self):
    return self.default_devel()
