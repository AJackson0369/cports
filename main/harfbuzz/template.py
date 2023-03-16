pkgname = "harfbuzz"
pkgver = "7.1.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dglib=enabled",
    "-Dfreetype=enabled",
    "-Dcairo=enabled",
    "-Dicu=enabled",
    "-Dgraphite2=enabled",
    "-Dintrospection=enabled",
    "-Ddocs=enabled",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gtk-doc-tools",
    "gobject-introspection",
    # prevent installing self through freetype
    "freetype-bootstrap",
]
makedepends = [
    "freetype-bootstrap", "cairo-devel", "graphite2-devel", "icu-devel"
]
pkgdesc = "Text shaping engine"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.freedesktop.org/wiki/Software/HarfBuzz"
source = f"https://github.com/{pkgname}/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "f135a61cd464c9ed6bc9823764c188f276c3850a8dc904628de2a87966b7077b"
# test failures since icu 71
options = ["!cross", "!check"]

def post_install(self):
    self.install_license("COPYING")

@subpackage("harfbuzz-devel")
def _devel(self):
    return self.default_devel()

@subpackage("harfbuzz-progs")
def _progs(self):
    return self.default_progs()
