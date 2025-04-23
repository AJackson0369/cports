pkgname = "fuse-overlayfs"
pkgver = "1.14"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
]
makedepends = [
    "fuse-devel",
    "linux-headers",
]
pkgdesc = "FUSE implementation for overlayfs"
license = "GPL-2.0-or-later"
url = "https://github.com/containers/fuse-overlayfs"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0779d1ee8fbb6adb48df40e54efa9c608e1d7bbd844800a4c32c110d5fcbe9f2"
hardening = ["vis", "cfi"]
