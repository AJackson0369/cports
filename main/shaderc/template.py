pkgname = "shaderc"
pkgver = "2022.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSHADERC_SKIP_TESTS=ON", "-DSHADERC_SKIP_EXAMPLES=ON"]
hostmakedepends = ["cmake", "ninja", "python", "pkgconf"]
makedepends = ["spirv-tools-devel", "spirv-headers", "glslang-devel"]
pkgdesc = "Collection of tools and libraries for shader compilation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/google/shaderc"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "517d36937c406858164673db696dc1d9c7be7ef0960fbf2965bfef768f46b8c0"
tool_flags = {
    "CXXFLAGS": [f"-I{self.profile().sysroot / 'usr/include/glslang'}"]
}

@subpackage("shaderc-progs")
def _progs(self):
    return self.default_progs()

@subpackage("shaderc-devel")
def _devel(self):
    return self.default_devel()
