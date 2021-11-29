pkgname = "fuse"
pkgver = "3.10.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dexamples=false", "-Duseroot=false"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["linux-headers", "eudev-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Linux FUSE (Filesystem in Userspace)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/libfuse/libfuse"
source = f"{url}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "b2e283485d47404ac896dd0bb7f7ba81e1470838e677e45f659804c3a3b69666"
suid_files = ["usr/bin/fusermount3"]
# ld: error: default version symbol fuse_loop_mt@@FUSE_3.2 must be defined
options = ["!lto"]

def do_check(self):
    self.do("python", "-m", "pytest", "test/", wrksrc = self.make_dir)

def post_install(self):
    self.chmod(self.destdir / "usr/bin/fusermount3", 0o4755)
    self.rm(self.destdir / "etc/init.d/fuse3")

@subpackage("fuse-static")
def _static(self):
    return self.default_static()

@subpackage("fuse-devel")
def _devel(self):
    return self.default_devel(man = True)
