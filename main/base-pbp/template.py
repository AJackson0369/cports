pkgname = "base-pbp"
pkgver = "0.1"
pkgrel = 1
archs = ["aarch64"]
depends = [
    "firmware-ap6256",
    "firmware-linux-rockchip",
    "u-boot-pinebook-pro-rk3399",
    "u-boot-menu",
]
pkgdesc = "Chimera base package for Pinebook Pro"
license = "custom:none"
url = "https://chimera-linux.org"


def install(self):
    self.install_file(self.files_path / "agetty", "etc/default")
    self.install_file(
        self.files_path / "60-pinebookpro.rules", "usr/lib/udev/rules.d"
    )
    self.install_file(
        self.files_path / "10-pinebookpro.hwdb", "usr/lib/udev/hwdb.d"
    )
    # u-boot-menu
    self.install_file(self.files_path / "u-boot-device", "etc/default")
    self.install_file(self.files_path / "u-boot-cmdline", "etc/default")
    # agetty service customization
    self.install_file(self.files_path / "agetty-ttyS2", "etc/default")
