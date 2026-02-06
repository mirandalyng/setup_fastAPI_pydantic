# Import:
from typing import Union
from fastapi import FastAPI, status
from schema.product import ProductSchema, CatogorySchema
import requests
from fastapi import HTTPException


# App variable
app = FastAPI(title="My first API")


# Create a root path


@app.get("/")
def root():
    return {"My root": "This is the root path"}


# # Simple array with products
# productList: list[ProductSchema] = [
#     ProductSchema(id=1, title="Macbook Air", price=1099.00,
#                   description="Apple: computer Model: MacbookAir M3chip", category="Electronics"),
#     ProductSchema(id=2, title="AirPods", price=129.99,
#                   description="Apple: Airpods Model: Generation 4", category="Electronics"),
#     ProductSchema(id=3, title="Galaxy14", price=99.99,
#                   description="Samsung: phone Model: Galaxy14 Pro Max Ultra", category="Electronics")

# ]


# Get all products
# @app.get("/products")
# def get_products():
#     return productList

# # user existing API
# @app.get("/products", response_model=list[ProductSchema])
# def get_API_products() -> list[ProductSchema]:
#     # 1 fetch data from the external API
#     response = requests.get("https://fakestoreapi.com/products")

#     # 2 check if the request was succesfull
#     if response.status_code != 200:
#         raise HTTPException(status_code=500, detail="external API error")

#     # 3 Parse the JSON data
#     procucts_data = response.json()

#     # Return the products data
#     return procucts_data


# @app.get("/products", response_model=list[ProductSchema])
# def get_products() -> list[ProductSchema]:
#     response = requests.get("https://fakestoreapi.com/products")
#     response_json = response.json()

#     products: list[ProductSchema] = []

#     for item in response_json:
#         product = ProductSchema(**item)
#         products.append(product)

    # return list(products)


# combination of the 2 above
@app.get("/products", response_model=list[ProductSchema])
def get_products_API() -> list[ProductSchema]:
    response = requests.get("https://fakestoreapi.com/products")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="External API error")

    response_json = response.json()

    products: list[ProductSchema] = []

    for item in response_json:
        product = ProductSchema(**item)
        products.append(product)

    return list(products)


# get the category names
@app.get("/categories", response_model=list[CatogorySchema])
def get_categories() -> list[CatogorySchema]:
    response = requests.get("https://fakestoreapi.com/products")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="External API error")

    response_json = response.json()

    categories: list[CatogorySchema] = []

    for item in response_json:
        category = CatogorySchema(**item)
        if category not in categories:
            categories.append(category)

    return list(categories)
