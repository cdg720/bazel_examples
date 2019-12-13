load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@foo_deps//:requirements.bzl", "requirement")

py3_image(
    name = "numpy_test",
    srcs = ["numpy_test.py"],
    deps = [
	requirement("numpy"),
    ],
    main = "numpy_test.py",
)
