pkgname = "llvm-bootstrap"
pkgver = "14.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release", "-Wno-dev",
    "-DCMAKE_INSTALL_PREFIX=/usr/lib/llvm-bootstrap",
    # use rpath so the installed tools always use their own libs
    "-DCMAKE_INSTALL_RPATH=/usr/lib/llvm-bootstrap/lib",
    # in sync with main/llvm
    "-DENABLE_LINKER_BUILD_ID=YES",
    "-DCOMPILER_RT_USE_BUILTINS_LIBRARY=YES",
    "-DLIBCXX_CXX_ABI=libcxxabi",
    "-DLIBCXX_USE_COMPILER_RT=YES",
    "-DLIBCXX_ENABLE_STATIC_ABI_LIBRARY=YES",
    "-DLIBCXX_HAS_MUSL_LIBC=YES",
    "-DLIBCXXABI_USE_LLVM_UNWINDER=YES",
    "-DLIBCXXABI_ENABLE_STATIC_UNWINDER=YES",
    "-DLIBCXXABI_USE_COMPILER_RT=YES",
    "-DLLVM_INSTALL_UTILS=YES",
    "-DLLVM_BUILD_LLVM_DYLIB=YES",
    "-DLLVM_LINK_LLVM_DYLIB=YES",
    "-DLLVM_ENABLE_RTTI=YES",
    "-DLLVM_ENABLE_PER_TARGET_RUNTIME_DIR=YES",
    "-DCLANG_DEFAULT_RTLIB=compiler-rt",
    "-DCLANG_DEFAULT_UNWINDLIB=libunwind",
    "-DCLANG_DEFAULT_CXX_STDLIB=libc++",
    "-DLLVM_ENABLE_LLD=YES",
    "-DLLVM_ENABLE_LIBCXX=YES",
    "-DLIBUNWIND_USE_COMPILER_RT=YES",
    # disable all the stuff we don't want and enable only some components
    "-DLLVM_ENABLE_LIBXML2=NO",
    "-DLLVM_ENABLE_LIBEDIT=NO",
    "-DLLVM_ENABLE_LIBPFM=NO",
    "-DLLVM_ENABLE_TERMINFO=NO",
    "-DCOMPILER_RT_BUILD_SANITIZERS=NO",
    "-DCOMPILER_RT_BUILD_XRAY=NO",
    "-DCOMPILER_RT_BUILD_LIBFUZZER=NO",
    "-DCOMPILER_RT_BUILD_PROFILE=NO",
    "-DCOMPILER_RT_BUILD_MEMPROF=NO",
    "-DLLVM_ENABLE_PROJECTS=clang;lld",
    "-DLLVM_ENABLE_RUNTIMES=compiler-rt;libcxx;libcxxabi;libunwind",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "perl", "python"]
makedepends = ["zlib-devel", "linux-headers"]
pkgdesc = "Low Level Virtual Machine (bootstrap)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://llvm.org"
source = f"https://github.com/llvm/llvm-project/releases/download/llvmorg-{pkgver}/llvm-project-{pkgver}.src.tar.xz"
sha256 = "1a3c2e57916c5a70153aaf0a0e6f1230d6368b9e0f4d04dcb9e039a31b1cd4e6"
debug_level = 0
# bootstrap; LTO would just slow it down, cross is unnecessary (not used
# in cross builds), debug info is unnecessary, and dependency/shlib scan
# would be actually harmful
options = [
    "!lto", "!cross", "!check", "!debug",
    "!scanshlibs", "!scanrundeps", "!autosplit",
]

cmake_dir = "llvm"

tool_flags = {
    "CFLAGS": ["-fPIC"],
    "CXXFLAGS": ["-fPIC"],
}

match self.profile().arch:
    case "x86_64": _arch = "X86"
    case "aarch64": _arch = "AArch64"
    case "ppc64le" | "ppc64": _arch = "PowerPC"
    case "riscv64": _arch = "RISCV64"
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"

configure_args += [
    "-DLLVM_TARGET_ARCH=" + _arch,
    "-DLLVM_HOST_TRIPLE=" + self.profile().triplet,
    "-DLLVM_DEFAULT_TARGET_TRIPLE=" + self.profile().triplet,
]

def post_install(self):
    # otherwise it'd use /usr/bin/ld by default
    self.install_link("ld.lld", "usr/lib/llvm-bootstrap/bin/ld")
    # cc/c++ symlinks
    self.install_link("clang", "usr/lib/llvm-bootstrap/bin/cc")
    self.install_link("clang++", "usr/lib/llvm-bootstrap/bin/c++")
