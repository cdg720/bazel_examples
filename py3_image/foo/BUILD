load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

py3_image(
    name = "hello_world_image",
    srcs = ["hello_world.py"],
    main = "hello_world.py",
)

py_binary(
    name = "hello_world_py",
    srcs = ["hello_world.py"],
    python_version = "PY3",
    main = "hello_world.py",
)
