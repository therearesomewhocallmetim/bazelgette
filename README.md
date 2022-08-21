# Attempt at Bazel

The goal of this project is to see how a `Bazel`-built repo can be organized, and to see how easy or hard it is to run the code from this repo on other computers, how much (or little) setup is required.

## Running the code

1. Clone this repo
2. Install `Bazelisk` ([Instructions](https://bazel.build/install/bazelisk))
3. Navigate to the root of the cloned repo
4. Run `bazel run '//projects/proj_one:main'` - this will run the project that displays the python version, uses an external dependency and the internal dependencies
5. Run `bazel test '...'` to run the tests
