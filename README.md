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
This will start a Docker container named `wikiwikiwrap` and expose it on port 5100.

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

## Code Formatting and Linting

To ensure that your code adheres to the project's style guidelines, you should run the code formatter and linter. This project uses ruff for both formatting and linting.

### Running the Code Formatter
To format your code, run the following command in your terminal:
```
make format
```

### Running the Linter

To check your code for any linting errors, run the following command in your terminal:

```
make lint
```

This command will check your code and report any issues it finds. If any issues are found, you should fix them before committing your code.

## Environment Variables

The application uses the following environment variables for configuration:

- `LOGGING_LEVEL`: The logging level for the application. Can be one of `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`. Defaults to `ERROR` in the production environment.

- `RATELIMIT_DEFAULT`: The default rate limit for the application, in the format `<number> per <unit>`, where `<number>` is the number of requests and `<unit>` is a time unit like `second`, `minute`, `hour`, or `day`. For example, `200 per minute` means 200 requests are allowed per minute. Defaults to `200 per minute` in the production environment.

- `STORAGE_URI`: The storage URI for the rate limiter. This should be a valid URL that points to the storage backend for the rate limiter. For example, `memory://` for an in-memory storage, `redis://localhost:6379` for a Redis backend. Defaults to `memory://` in the production environment, but should use redis in a real setup.
