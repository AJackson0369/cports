pkgname = "libbytesize"
pkgver = "2.7"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "python", "gettext-tiny"]
makedepends = ["gmp-devel", "mpfr-devel", "pcre2-devel"]
pkgdesc = "Library for operations with sizes in bytes"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/storaged-project/libbytesize"
source = f"https://github.com/storaged-project/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "8bae8287af6ef5624c320f70defdcd84ddc0c2057d3b59a5871897f27697811e"
# cba
options = ["!check"]

@subpackage("libbytesize-devel")
def _devel(self):
    self.depends += ["gmp-devel", "mpfr-devel"]

    return self.default_devel()

@subpackage("libbytesize-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python", "python-six"]

    return ["usr/lib/python*"]
