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

### Run the app

```
$ fastapi run dev main.py
```

Visit : localhost:8000

### Psycopg3 installation

```
$ uv add "psycopg[binary]"
$ uv add "psycopg[pool]"
```

## Main

**Import:**

```
from typing import Union
from fastapi import FastAPI, status

#Example for importing schema
from schema.product import ProductSchema

import requests

```

## User Schema

**Import:**

```
from pydantic import BaseModel
```
