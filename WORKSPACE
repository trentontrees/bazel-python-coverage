load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "e85ae30de33625a63eca7fc40a94fea845e641888e52f32b6beea91e8b1b2793",
    strip_prefix = "rules_python-0.27.1",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.27.1/rules_python-0.27.1.tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_multi_toolchains")

py_repositories()

default_python_version = "3.11"

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
