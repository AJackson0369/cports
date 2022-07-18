pkgname = "libxo"
pkgver = "1.6.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-dependency-tracking", "--disable-static"]
hostmakedepends = ["pkgconf", "gettext-tiny"]
makedepends = ["gettext-tiny-devel", "musl-bsd-headers"]
pkgdesc = "Library for generating text, XML, JSON, and HTML output"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://github.com/Juniper/libxo"
source = f"https://github.com/Juniper/{pkgname}/releases/download/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "9f2f276d7a5f25ff6fbfc0f38773d854c9356e7f985501627d0c0ee336c19006"
tool_flags = {"CFLAGS": ["-Wno-unused-command-line-argument"]}

# libxo does not respect LDFLAGS, so hack it in
def init_configure(self):
    tcflags = self.get_cflags(shell = True)
    tlflags = self.get_ldflags(shell = True)

    self.configure_env = {"CFLAGS": f"{tcflags} {tlflags}"}

@subpackage("libxo-devel")
def _devel(self):
    return self.default_devel()

@subpackage("libxo-progs")
def _progs(self):
    return self.default_progs()
