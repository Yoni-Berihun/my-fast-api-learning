#importing the module 
from fastapi import FastAPI
from pydantic import BaseModel

class Profile(BaseModel):
    name:str
    email:str
    age:int


#creating instance of the class fast API
app = FastAPI()

@app.post('/adduser')
def adduser(profile:Profile):
    return profile
