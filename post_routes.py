from fastapi import FastAPI
from pydantic import BaseModel
from typing import Set, List
from uuid import UUID
from datetime import date,datetime,time,timedelta


class Event(BaseModel):
    event_id :UUID
    start_date: date
    start_time: datetime
    end_time:datetime
    repeat_time :time
    execute_after : timedelta

class Profile(BaseModel):
    name: str
    email: str
    age: int

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

class Offer(BaseModel):
    name: str
    description: str
    price: float
    products: List[Product]

class User(BaseModel):
    name: str
    email: str

class PurchaseRequest(BaseModel):
    user: User
    product: Product

app = FastAPI()

@app.post("/offer")
def addoffer(offer: Offer):
    return {"offer": offer}

@app.post("/purchase")
def purchase(data: PurchaseRequest):
    return {"user": data.user, "product": data.product}

@app.post("/adduser")
def adduser(profile: Profile):
    return profile

@app.post("/addproduct/{product_id}")
def addproduct(product: Product, product_id: int, category: str):
    product.discounted_price = product.price - (product.price * product.discount) / 100
    return {"Product_Id": product_id, "Product": product, "category": category}
