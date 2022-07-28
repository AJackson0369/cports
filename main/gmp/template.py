pkgname = "gmp"
pkgver = "6.2.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-cxx"]
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "Library for arbitrary precision arithmetic"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later OR GPL-2.0-or-later"
url = "https://gmplib.org"
source = f"{url}/download/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "fd4829912cddd12f84181c3451cc752be224643e87fac497b69edddadc49b4f2"

@subpackage("gmpxx")
def _cxx(self):
    self.pkgdesc = f"{pkgdesc} (C++ support)"

    return ["usr/lib/libgmpxx.so.*"]

@subpackage("gmpxx-devel")
def _cxxdevel(self):
    self.pkgdesc = f"{pkgdesc} (C++ development files)"

    return [
        "usr/include/gmpxx.h",
        "usr/lib/libgmpxx.*",
        "usr/lib/pkgconfig/gmpxx.pc",
    ]

@subpackage("gmp-devel")
def _devel(self):
    return self.default_devel()
