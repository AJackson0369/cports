pkgname = "libgusb"
pkgver = "0.4.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false", "-Dintrospection=true"]
hostmakedepends = ["meson", "pkgconf", "vala", "gobject-introspection"]
makedepends = [
    "libglib-devel", "libusb-devel", "libgudev-devel", "json-glib-devel",
    "vala-devel", "usbutils"
]
pkgdesc = "GLib wrapper around libusb"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/hughsie/libgusb"
source = f"{url}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "bc8c6328289f057c8f73b07c1ba6251de96029787309f2672ca252ca90ace1b2"
# no access to usb in container
options = ["!check", "!cross"]

@subpackage("libgusb-devel")
def _devel(self):
    return self.default_devel()
