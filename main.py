#exercise one Path paramenter

from fastapi import FastAPI
from pydantic import BaseModel
 
app=FastAPI()
@app.get('/user/{id:int}')
def user(id):
     return {"message":f"user with id {id}"}

#exercise two query parameter

@app.get('/items')
def items(page:int, limit:int):
    return {"page":page, 
            "limit":limit
           }
#exercise three Request body(Pydantic) 
class Student(BaseModel):
    name:str
    score:int
    result:int
    
@app.post('/students')
def student(student:Student):
    return student 
 
 #exercise four Using model inside a function
class Undergraduate(BaseModel):
    name:str
    score:int
    result:None
@app.post('/undergraduate')
def transcript(undergraduate:Undergraduate):
    if undergraduate.score >= 50:
        undergraduate.result="Pass"
    else:
        undergraduate.result="Fail"
    return undergraduate

#exercise five path +query+ request body
class Order(BaseModel):
    item_name:str
    price:int
    quantity:int
    total_price:None
class Customer(BaseModel):
    name:str

@app.post('/orders/{order_id}')
def order_detail(
    order:Order,
    order_id:int,
    customer:str
):
    order.total_price=order.price*order.quantity
    return{"order_id" :order_id,"customer":customer,"order":order}
 