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
def products(id =1,price=0):
    return {f'product with and id: {id} and price :{price}'}

#we can also give specific data type and also
# provide default values for the query parameter
@app.get('/items')
def items(id:int=1, qty:int=0):
    return{f'item with an id:{id} and with quuantity of:{qty}'}

#using path and query parametres simoultaneously
@app.get('/about/{userid}/comments')
def about(userid:int,commentid:int):
    return{f'About page for the user with user id: {userid} and comment with: {commentid}'}
#this is how we use to add it on browses http://127.0.0.1:8000/about/224/comments?commentid=98

#required query parametres
