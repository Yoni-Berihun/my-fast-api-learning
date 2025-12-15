#importing the module 
from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
    name:str
    email:str
    age:int


class Product(BaseModel):
    name:str
    price:int
    discount:int
    discounted_price:int
    
#creating instance of the class fast API
app = FastAPI()

@app.post('/adduser')
def adduser(profile:Profile):
    return profile
#using model inside a function
@app.post('/addproduct')
def addproduct(product:Product):
    product.discounted_price = product.price - (product.price * product.discount)/100
    return product