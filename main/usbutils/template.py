pkgname = "usbutils"
pkgver = "015"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
makedepends = ["udev-devel", "libusb-devel", "linux-headers"]
depends = ["hwdata-usb"]
pkgdesc = "Linux USB utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "http://linux-usb.sourceforge.net"
source = f"$(KERNEL_SITE)/utils/usb/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c3b451bb1f4ff9f6356cac5a6956a9ac8e85d81651af56a29e689f94fa6fda6e"
hardening = ["vis", "cfi"]

def pre_configure(self):
    self.do("autoreconf", "-if")

def post_install(self):
    self.rm(self.destdir / "usr/bin/lsusb.py")
