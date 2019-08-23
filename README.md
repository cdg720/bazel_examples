# bazel_examples

I have tested my examples with bazel 0.28.1 and macOS Mojave.

Every directory is a self-contained example.

## py_binary
```bash
cd py_binary
bazel run -c opt foo:hello_world  # builds and runs a python binary of hello_world.py.
```

## py3_image
You need [docker](https://docs.docker.com/install/) to run the below command.
```bash
cd py3_image
bazel run -c opt foo:hello_world  # builds and runs a docker image of hello_world.py.
```
