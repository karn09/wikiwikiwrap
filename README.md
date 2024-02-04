# WikiWikiWrap

WikiWikiWrap is a Python project that acts an example of

## Installation

This project uses python 3.12.1. I use `pyenv` to manage my python versions. That can be installed via `brew install pyenv`. Install 3.12.1 using `pyenv install 3.12.1`.

To set up the project:

```
brew install pyenv # if you do not already have it.
pyenv install 3.12.1
make setup
```

## Usage

To run the Flask development server:
```
make dev
```
To build the Docker container:
```
make build
```

To run the Docker container:
```
make run
```
This will start a Docker container named `wikiwikiwrap` and expose it on port 5000.

## Running Tests

To run tests:

```
make test
```

To run tests and display a coverage report:
```
make coverage-run
```

To display a coverage report:
```
make coverage
```

## Cleaning Up

To stop and remove the Docker container:
```
make clean
```
