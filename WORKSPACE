load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "d71d2c67e0bce986e1c5a7731b4693226867c45bfe0b7c5e0067228a536fc580",
    strip_prefix = "rules_python-0.29.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.29.0/rules_python-0.29.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_multi_toolchains")

py_repositories()

default_python_version = "3.12"

python_register_multi_toolchains(
    name = "python",
    default_version = default_python_version,
    python_versions = [
        "3.11",
        "3.12",
    ],
    register_coverage_tool = True,
)

load("@python//:pip.bzl", "multi_pip_parse")
load("@python//3.11:defs.bzl", interpreter_3_11 = "interpreter")
load("@python//3.12:defs.bzl", interpreter_3_12 = "interpreter")

multi_pip_parse(
    name = "pip_deps",
    default_version = default_python_version,
    python_interpreter_target = {
        "3.11": interpreter_3_11,
        "3.12": interpreter_3_12,
    },
    requirements_lock = {
        "3.11": "//py:requirements_lock.txt",
        "3.12": "//py:requirements_lock.txt",
    },
)

load("@pip_deps//:requirements.bzl", "install_deps")

install_deps()
