pkgname = "wayland"
pkgver = "1.19.0"
pkgrel = 0
build_style = "meson"
# "Tests must not be built with NDEBUG defined, they rely on assert()."
configure_args = ["-Ddocumentation=false", "-Db_ndebug=false"]
hostmakedepends = ["meson", "pkgconf", "flex"]
makedepends = [
    "libexpat-devel", "libffi-devel", "libfl-static", "libxml2-devel"
]
pkgdesc = "Wayland compositor infrastructure"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://wayland.freedesktop.org"
source = f"{url}/releases/{pkgname}-{pkgver}.tar.xz"
sha256 = "baccd902300d354581cd5ad3cc49daa4921d55fb416a5883e218750fef166d15"

if self.cross_build:
    hostmakedepends += ["wayland-progs"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("wayland-progs")
def _progs(self):
    return self.default_progs(extra = [
        "usr/share/aclocal/wayland-scanner.m4",
        "usr/share/wayland/wayland-scanner.mk",
    ])

@subpackage("wayland-static")
def _static(self):
    return self.default_static()

@subpackage("wayland-devel")
def _devel(self):
    self.depends += [
        f"wayland-progs={pkgver}-r{pkgrel}",
        "libffi-devel"
    ]
    return self.default_devel(extra = ["usr/share"])
