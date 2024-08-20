pkgname = "libcdio-paranoia"
_v1 = "10.2"
_v2 = "2.0.2"
pkgver = f"{_v1}.{_v2}"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-example-progs", "--enable-cpp-progs"]
make_cmd = "gmake"
# out of tree build is broken
make_dir = "."
hostmakedepends = ["automake", "libtool", "gmake", "pkgconf"]
makedepends = ["libcdio-devel", "linux-headers"]
pkgdesc = "CD paranoia utility/libraries from libcdio"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/libcdio"
source = f"$(GNU_SITE)/libcdio/libcdio-paranoia-{_v1}+{_v2}.tar.bz2"
sha256 = "186892539dedd661276014d71318c8c8f97ecb1250a86625256abd4defbf0d0c"


@subpackage("libcdio-paranoia-devel")
def _(self):
    return self.default_devel()


@subpackage("libcdio-paranoia-progs")
def _(self):
    return self.default_progs()
