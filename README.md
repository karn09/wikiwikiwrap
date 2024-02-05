# WikiWikiWrap

WikiWikiWrap is a Python project that acts an example of Flask app to wrap the Wikipedia views endpoint.

## Calling the Wikipedia Views Endpoint

The Wikipedia views endpoint allows you to get the number of views for a specific Wikipedia article for a given month and year.

Here's how you can call this endpoint:

1. Construct the URL for the endpoint. The URL should be in the following format:
```
http://<your-server-url>/views/<article>/<year>/<month>
```

Replace <your-server-url> with the URL of your server, <article> with the name of the Wikipedia article, <year> with the 4-digit year, and <month> with the 2-digit month.

For example, to get the views for the "Python" article for January 2020, the URL would be:

```
http://<your-server-url>/views/Python/2020/01
```

2. Send a GET request to the constructed URL. You can do this using a tool like curl or Postman, or from your application code.

Here's how to do it with `curl`:
```
curl http://<your-server-url>/views/Python/2020/01
```

The server will respond with a JSON object containing the views data. If there was an error, the server will respond with a JSON object containing an error message.


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
