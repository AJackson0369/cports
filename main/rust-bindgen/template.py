pkgname = "rust-bindgen"
pkgver = "0.70.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bins"]
make_install_args = ["--bins"]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["clang-libs"]
checkdepends = ["clang-libs"]
pkgdesc = "Tool to generate Rust bindings for C/C++ code"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://rust-lang.github.io/rust-bindgen"
source = f"https://github.com/rust-lang/rust-bindgen/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "9afd95f52c55147c4e01976b16f8587526f0239306a5a4610234953ab2ee7268"
# needs rustfmt nightly to run suite
options = ["!check"]


def do_install(self):
    self.install_bin(f"./target/{self.profile().triplet}/release/bindgen")
    self.install_license("LICENSE")
