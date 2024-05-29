# decisionpy

Implementations of various decision-making models in Python.

## Toolchain

This project is built with the following software:

- [Poetry](https://python-poetry.org/) for dependency management and deployment;
- [Black](https://github.com/psf/black) for code formatting;
- [Pylint](https://github.com/pylint-dev/pylint) to detect programming mistakes before execution;
- [pytest](https://docs.pytest.org) for unit testing;
- A [GitHub Action](.github/workflows/ci.yaml) to check the code upon each push.

## Development notes

Here are some useful commands for running this project:

```bash
# Reformat all Python files
black .

# Check the code for mistakes
pylint decisionpy tests

# Run all unit tests
pytest
```

## License

[MIT](LICENSE).

Copyright © 2024-present [Baptiste Pesquet](https://bpesquet.fr).
