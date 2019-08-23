# bazel_examples

I have tested examples with bazel 0.28.1 and macOS Mojave.

Every directory is a self-contained example.

## py_binary
```bash
cd py_binary
# Builds and runs a python binary of hello_world.py.
bazel run -c opt foo:hello_world  
```

## py3_image
You need [docker](https://docs.docker.com/install/) to run the command below.
```bash
cd py3_image
# Builds and runs a docker image of hello_world.py.
bazel run -c opt foo:hello_world \
  --extra_toolchains=//platform_defs:my_platform_python_toolchain \
  --host_platform=//platform_defs:my_platform

# Builds and runs a python binary of hello_world.py using toolchain.
bazel run -c opt //foo:hello_world_py \
  --extra_toolchains=//platform_defs:my_platform_python_toolchain \
  --host_platform=//platform_defs:my_platform \
  --platforms=//platform_defs:my_platform
```
