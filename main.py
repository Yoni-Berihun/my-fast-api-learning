#importing the module 
from fastapi import FastAPI

#creating instance of the class fast API
app = FastAPI()

@app.get('/')
def index():
    return 'Hello there!'

@app.get('/property')
def property():
    return 'this is proeprty page'

@app.get('/movies')
def movies():
    return {'movie list': {'movie 1', 'movie 2'}}


#this is a path parameter
@app.get('/person/{id}')
def person(id):
    return {f'This is a personal page for person {id}'}

#this is a path parameter with data type specified
@app.get('/persons/{id}')
def persons(id:int):
    return {f'This is a personal page for person {id}'}

#this is a path parameter with string this will always consider the value 
# after /profile/ as a string always.
@app.get('/profile/{username}')
def profile(username:str):
    return {f'this is the profile page for user : {username}'}