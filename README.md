# bazel_examples

I have tested examples with bazel 2.0.0 and macOS Catalina.

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
bazel run -c opt foo:hello_world_image
```

## numpy
```bash
cd numpy
# Builds and runs a docker image of numpy_test.py. (It fails right now.)
bazel run -c opt foo:numpy_test
```
