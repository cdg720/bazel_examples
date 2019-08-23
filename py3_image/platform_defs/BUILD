load("@bazel_tools//tools/python:toolchain.bzl", "py_runtime_pair")

constraint_value(
    name = "usr_weirdpath_python3",
    constraint_setting = "@bazel_tools//tools/python:py3_interpreter_path",
)

# A definition of a platform whose Python interpreters are under these paths.

platform(
    name = "my_platform",
    constraint_values = [
        "@bazel_tools//platforms:osx",
        "@platforms//cpu:x86_64",
        ":usr_weirdpath_python3",
    ],
)

# Python runtime definitions that reify these system paths as BUILD targets.

py_runtime(
    name = "my_platform_py3_runtime",
    interpreter_path = "/usr/local/bin/python3",
    python_version = "PY3",
)

py_runtime_pair(
    name = "my_platform_runtimes",
    py3_runtime = ":my_platform_py3_runtime",
)

# A toolchain definition to expose these runtimes to toolchain resolution.

toolchain(
    name = "my_platform_python_toolchain",
    # Since the Python interpreter is invoked at runtime on the target
    # platform, there's no need to specify execution platform constraints here.
    target_compatible_with = [
        # Make sure this toolchain is only selected for a target platform that
        # advertises that it has interpreters available under /usr/weirdpath.
        # ":usr_weirdpath_python2",
        ":usr_weirdpath_python3",
    ],
    toolchain = ":my_platform_runtimes",
    toolchain_type = "@bazel_tools//tools/python:toolchain_type",
)
