[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

# Playground

A playground for testing GitHub, Python packaging and CI related stuff

## Development

Using Makefile:
```
make venv
source venv/bin/activate
make linters
```

Or, using Invoke:
```
./build-venv
source venv/bin/activate
invoke linters
```
