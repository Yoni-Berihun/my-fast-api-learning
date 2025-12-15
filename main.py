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

##################################################################

#ordering of routes
@app.get('/user/admin')
def admin():
    return{'This is admin page'}

@app.get('/user/{name}')
def page(name):
    return{f'this is a profile page for user {name}'}
####################################################################

#query parametres
@app.get('/products')
def products(id,price):
    return {f'product with and id: {id},{price}'}
