pkgname = "xapian-core"
pkgver = "1.4.26"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "zlib-ng-compat-devel",
]
pkgdesc = "Open source search engine library"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://xapian.org"
source = f"https://oligarchy.co.uk/xapian/{pkgver}/xapian-core-{pkgver}.tar.xz"
sha256 = "9e6a7903806966d16ce220b49377c9c8fad667c8f0ffcb23a3442946269363a7"
hardening = ["vis", "cfi"]
# see below
options = []

if self.profile().arch == "ppc64":
    # FIXME: hangs after replacedoc9
    options += ["!check"]


@subpackage("xapian-core-devel")
def _devel(self):
    return self.default_devel()


@subpackage("xapian-core-libs")
def _libs(self):
    return self.default_libs()
