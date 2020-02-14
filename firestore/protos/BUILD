package(default_visibility = [
    "//foo:__pkg__",
])

load("@build_stack_rules_proto//python:python_proto_library.bzl", "python_proto_library")
load("@rules_proto//proto:defs.bzl", "proto_library")

proto_library(
    name = "empty_proto",
    srcs = ["empty.proto"],
)

python_proto_library(
    name = "empty_py",
    deps = [ ":empty_proto" ],
)
