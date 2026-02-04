from pydantic import BaseModel


class RateProcuctSchema(BaseModel):
    rate: float
    count: int


class ProductSchema(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: RateProcuctSchema
