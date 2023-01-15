pkgname = "libarchive"
pkgver = "3.6.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-acl", "--enable-xattr", "--without-expat",
    "--with-lz4", "--with-openssl", "--without-xml2",
    "--without-nettle", "--disable-rpath"
]
hostmakedepends = ["pkgconf"]
makedepends = [
    "zlib-devel", "libbz2-devel", "liblzma-devel",
    "acl-devel", "liblz4-devel", "openssl-devel"
]
pkgdesc = "Library to read/write several different streaming archive formats"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "http://www.libarchive.org"
source = f"https://github.com/libarchive/libarchive/releases/download/v{pkgver}/libarchive-{pkgver}.tar.gz"
sha256 = "c676146577d989189940f1959d9e3980d28513d74eedfbc6b7f15ea45fe54ee2"
# unmarked api
hardening = ["!vis"]
# encoding failures on musl; harmless
options = ["bootstrap", "!check"]

if self.stage > 0:
    configure_args.append("--with-zstd")
    makedepends.append("libzstd-devel")
else:
    configure_args.append("--without-zstd")

def post_install(self):
    self.install_license("COPYING")
    with self.pushd(self.destdir):
        self.mv("usr/bin/bsdtar", "usr/bin/tar")
        self.mv("usr/bin/bsdcpio", "usr/bin/cpio")
        with self.pushd("usr/share/man/man5"):
            self.mv("mtree.5", "libarchive-mtree.5")

@subpackage("bsdtar")
def _bsdtar(self):
    self.pkgdesc = "BSD utilities using libarchive"

    return self.default_progs(man = "15")

@subpackage("libarchive-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()
