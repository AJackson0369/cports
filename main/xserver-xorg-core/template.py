pkgname = "xserver-xorg-core"
pkgver = "21.1.1"
pkgrel = 0
build_style = "meson"
_fontroot = "/usr/share/fonts"
configure_args = [
    "-Dxorg=true", "-Dxephyr=true", "-Dxnest=true", "-Dxvfb=true",
    "-Dipv6=true", "-Dxcsecurity=true", "-Ddri3=true", "-Dglamor=true",
    "-Dglx=true", "-Dsystemd_logind=true", "-Dsuid_wrapper=true",
    "-Dlinux_acpi=true", "-Dudev=true",
    "-Dlinux_apm=false", "-Dhal=false",
    "-Dxkb_dir=/usr/share/X11/xkb", "-Dxkb_output_dir=/var/lib/xkb",
]
hostmakedepends = ["meson", "pkgconf", "xkbcomp", "flex"]
makedepends = [
    "libxfont2-devel", "libxkbfile-devel", "libxshmfence-devel",
    "libxcb-devel", "libxrender-devel", "libxv-devel", "libxtst-devel",
    "libxres-devel", "libxxf86dga-devel", "libxkbui-devel", "libtirpc-devel",
    "mesa-devel", "libepoxy-devel", "pixman-devel", "nettle-devel",
    "dbus-devel", "openssl-devel", "font-util-devel", "xkbcomp",
    "xorgproto", "xtrans", "xcb-util-devel", "xcb-util-image-devel",
    "xcb-util-keysyms-devel", "xcb-util-renderutil-devel", "xcb-util-wm-devel",
    "libxcvt-devel",
]
checkdepends = ["xkeyboard-config"]
depends = ["xserver-common>=0", "xkeyboard-config", "elogind"]
provides = [
    "xserver-abi-extension=10.0",
    "xserver-abi-input=24.4",
    "xserver-abi-video=25.2"
]
pkgdesc = "X.org X server"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT AND BSD-3-Clause"
url = "https://xorg.freedesktop.org"
source = f"https://gitlab.freedesktop.org/xorg/xserver/-/archive/xorg-server-{pkgver}/xserver-xorg-server-{pkgver}.tar.gz"
sha256 = "14b51c6e54362f73d09700738a5dc7540482b2c22eb1edaf8df5185e01edafc7"
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE", "-D__uid_t=uid_t", "-D__gid_t=gid_t"],
    "LDFLAGS": ["-Wl,-z,lazy"] # must be set for modules to work
}
suid_files = [
    "usr/libexec/Xorg.wrap"
]
# test times out
options = ["!check"]

match self.profile().arch:
    case "x86_64":
        configure_args += ["-Dint10=x86emu"]
    case _:
        configure_args += ["-Dint10=false"]

_fontpaths = []

for fp in [
    "misc", "100dpi:unscaled", "75dpi:unscaled", "TTF", "Type1"
]:
    _fontpaths.append(f"/usr/share/fonts/{fp}")

configure_args.append(f"-Ddefault_font_path=" + ",".join(_fontpaths))

def post_install(self):
    self.install_license("COPYING")

    self.chmod(self.destdir / "usr/libexec/Xorg.wrap", mode = 0o4755)

@subpackage("xserver-xorg-xnest")
def _xnest(self):
    self.pkgdesc = "Nested X server that runs as an X application"

    return [
        "usr/bin/Xnest", "usr/share/man/man1/Xnest.1"
    ]

@subpackage("xserver-xorg-xephyr")
def _xephyr(self):
    self.pkgdesc = "X server outputting to a window on a pre-existing display"

    return [
        "usr/bin/Xephyr", "usr/share/man/man1/Xephyr.1"
    ]

@subpackage("xserver-xorg-xvfb")
def _xvfb(self):
    self.pkgdesc = "Virtual framebuffer X server"
    self.depends += ["xkeyboard-config"]

    return [
        "usr/bin/Xvfb", "usr/share/man/man1/Xvfb.1"
    ]

@subpackage("xserver-common")
def _common(self):
    self.pkgdesc = f"{pkgdesc} (common files)"

    return ["usr/lib/xorg/protocol.txt"]

@subpackage("xserver-xorg-devel")
def _devel(self):
    self.depends += [
        "xorgproto", "xtrans", "libxfont2-devel", "libxkbfile-devel",
        "libxshmfence-devel", "libxcb-devel", "libxrender-devel",
        "libxrandr-devel", "libxi-devel", "libpciaccess-devel",
    ]
    return self.default_devel()
