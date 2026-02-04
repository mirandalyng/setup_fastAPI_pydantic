# SetUp FastAPI & Pydantic

## Create an uv enviroment

### Command in root-folder

- Creates an toml-file
- Creates virtual enviroment

```
$ uv init
```

### Command to install fastAPI

- [standard] includes:
  (Uvicorn, pydantic, python-multipart)

```
$ uv add "fastapi[standard]"
```

### Command to add requests file

```
$ uv add requests
```
