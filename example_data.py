from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Set

app = FastAPI()

class Image(BaseModel):
    url: str
    name: str

class Product(BaseModel):
    name: str
    price: int
    discount: int
    discounted_price: int
    tags: Set[str] = set()
    image: List[Image]

    class Config:
        schema_extra = {
            "example": {
                "name": "Mobile Phone",
                "price": 20000,
                "discount": 15,
                "discounted_price": 0,
                "tags": ["electronics", "productivity"],
                "image": [
                    {"url": "https://www.google.com", "name": "google"},
                    {"url": "https://www.hu.edu.et", "name": "Hawassa University"}
                ]
            }
        }

@app.post("/addproduct/")
def addproduct(product: Product):
    return product
