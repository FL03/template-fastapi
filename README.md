# template-fastapi

[![Docker](https://github.com/FL03/template-fastapi/actions/workflows/docker.yml/badge.svg)](https://github.com/FL03/template-fastapi/actions/workflows/docker.yml)

***

synapse is built leveraging OpenAI's API to create a data-fluid experience enabling users to make informed decisions regardless of the environment. The microservice is written in Python and built with FastAPI.

## Getting Started

### Building from the Source

Make sure you have poetry installed on your host system

#### *Clone the repository*

```bash
git clone https://github.com/FL03/template-fastapi
```

#### *Setup the environment*

```bash
poetry install
```

#### *Start the application*

```bash
poetry run python -m synapse
```

### Docker

Make sure you have docker installed on the target system

#### *Pull the image*

```bash
docker pull jo3mccain/template-fastapi:latest
```

#### *Build the image locally (optional)*

```bash
docker buildx build --tag jo3mccain/template-fastapi:latest .
```

#### *Run the image*

```bash
docker run -p 8080:8080 jo3mccain/template-fastapi:latest
```

## Usage

## Contributors

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

- [Apache-2.0](https://choosealicense.com/licenses/apache-2.0/)
- [MIT](https://choosealicense.com/licenses/mit/)
