# bazel-python-coverage

This is a repository to investigate the behavior of python coverage.
You can get coverage report with the following commands:

```
bazel coverage --combined_report=lcov //apps/demo/...
```

To generate html, run the command:

```
genhtml --branch-coverage --output genhtml "$(bazel info output_path)/_coverage/_coverage_report.dat"
```
