pkgname = "libcgroup"
pkgver = "3.2.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--disable-systemd",
]
hostmakedepends = [
    "automake",
    "flex",
    "libtool",
    "pkgconf",
]
makedepends = [
    "chimerautils-devel",
    "linux-headers",
    "linux-pam-devel",
]
checkdepends = ["bash"]
pkgdesc = "Cgroup library and commandline utilities for managing cgroups"
license = "LGPL-2.1-only"
url = "https://github.com/libcgroup/libcgroup"
source = f"{url}/releases/download/v{pkgver}/libcgroup-{pkgver}.tar.gz"
sha256 = "9a0fc2d6c377215c3e0d849f9189ecd91fd075f1da0a24b73f56c8892e86bdfe"
# vis breaks symbols
hardening = []
# tests need.. sudo..
options = ["!check", "linkundefver"]


def post_install(self):
    # nuke suid
    (self.destdir / "usr/bin/cgexec").chmod(0o755)


@subpackage("libcgroup-devel")
def _(self):
    return self.default_devel()


@subpackage("libcgroup-progs")
def _(self):
    return self.default_progs()


@subpackage("libcgroup-pam")
def _(self):
    self.subdesc = "PAM"
    self.depends = [self.parent, "linux-pam"]
    self.install_if = [self.parent, "linux-pam"]
    # transitional
    self.provides = [self.with_pkgver("pam_cgroup")]
    return [
        "usr/lib/security",
    ]
