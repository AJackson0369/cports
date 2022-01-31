pkgname = "eog"
pkgver = "41.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dintrospection=true"]
hostmakedepends = [
    "meson", "pkgconf", "gobject-introspection", "glib-devel", "gettext-tiny",
    "itstool",
]
makedepends = [
    "libglib-devel", "gtk+3-devel", "gnome-desktop-devel", "libpeas-devel",
    "gdk-pixbuf-devel", "libexif-devel", "exempi-devel", "lcms2-devel",
    "libportal-devel", "libjpeg-turbo-devel", "librsvg-devel",
]
depends = ["hicolor-icon-theme", "shared-mime-info"]
provides = ["so:libeog.so=0"]
pkgdesc = "GNOME image viewer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/EyeOfGnome"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "86e1b9ba39dacf74226afa457ab983b41253b89f617bf54139cad0892d02d8a9"

@subpackage("eog-devel")
def _devel(self):
    return self.default_devel()
