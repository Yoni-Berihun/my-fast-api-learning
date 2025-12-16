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
    
class User(BaseModel):
    name:str
    email:str
       
#creating instance of the class fast API
app = FastAPI()

@app.post('/purchase')
def purchase(user:User,product:Product):
    return {"user": user, "product":product}

@app.post('/adduser')
def adduser(profile:Profile):
    return profile
#using model inside a function
@app.post('/addproduct/{product_id}')
def addproduct(product:Product, product_id:int, category:str):
    product.discounted_price = product.price - (product.price * product.discount)/100
    return {"Product_Id":product_id, "Product":product, 'category':category}