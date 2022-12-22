pkgname = "u-boot-qemu_arm64"
pkgver = "2022.10"
pkgrel = 0
build_style = "u_boot"
hostmakedepends = [
    "gmake", "gcc-aarch64-none-elf", "flex", "bison",
    "dtc", "python", "openssl-devel"
]
pkgdesc = "U-Boot for qemu-aarch64"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND BSD-3-Clause"
url = "https://www.denx.de/wiki/U-Boot"
source = f"https://ftp.denx.de/pub/u-boot/u-boot-{pkgver}.tar.bz2"
sha256 = "50b4482a505bc281ba8470c399a3c26e145e29b23500bc35c50debd7fa46bdf8"
env = {
    "U_BOOT_TRIPLET": "aarch64-none-elf",
    "U_BOOT_TARGETS": "u-boot",
}
# not relevant
options = ["!strip", "!check", "!lto", "!debug", "foreignelf"]

# FIXME visibility
hardening = ["!vis"]
