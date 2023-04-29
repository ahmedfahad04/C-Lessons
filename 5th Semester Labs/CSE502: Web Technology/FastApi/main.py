from typing import Union
from fastapi import FastAPI
from model import Item
from enum import Enum

# create an instance of FastAPI,
# FastAPI is a Python class that provides all the functionality for your API.
app = FastAPI()


#################### BASIC ####################


# Create path operation decorator with the path /.
# A "path" is also commonly called an "endpoint" or a "route".
@app.get('/')
async def read_root():
    return {'Hello': 'Worlds'}



#################### PATH PARAMETERS ####################


# => 1
# path operation with PATH PARAMETERS (item_id, q)
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {
        "item_id": item_id
    }
    
# ?------------------------------------------------------
   
# => 2 
# path operation with PATH PARAMETERS (item_id, q) with type
@app.get("/items/{item_id}/{q}")
async def read_item(item_id: int, q: str):
    return {
        "item_id": item_id, "q": q
    }
    
# ?------------------------------------------------------
   
# => 3 
# path operations are evaluated in order, you need to make sure that 
# the path for /users/me is declared before the one for /users/{user_id}:
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
# !Otherwise, the path for /users/{user_id} would match also for 
# !/users/me, "thinking" that it's receiving a parameter user_id with a value of "me".

# ?------------------------------------------------------

# =>4
# We cannot redefine a path operation
@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]

# it won't execute
@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]

# ?------------------------------------------------------

# =>5
# Predefined Path Parameters Value using ENUM
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# ?------------------------------------------------------

# =>6
# Path Pramater Containing Paths (using Path Converter)
@app.get("/files/{file_path:path}")  #! becareful, you can't give space between the : here.
async def read_file(file_path: str):
    return {"file_path": file_path}



#################### QUERY PARAMETERS ####################


# =>1
# Parameter that are not part of the path, they are called "query parameters".
'''
http://127.0.0.1:8000/items/?skip=0&limit=10

...the query parameters are:

skip: with a value of 0
limit: with a value of 10
'''

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 2):
    return fake_items_db[skip : skip + limit]

# ?------------------------------------------------------

# =>2
# Optional Parameters (name will be optional and will be None by default. This params start with ?)
@app.get("/prod/")
async def read_item(skip: int = 0, limit: int = 2, quant: Union[str, None] = None):
    return fake_items_db[skip : skip + limit] + [{"quant": quant}]

# ?------------------------------------------------------

# =>3
# Query parameter type conversion (short = 1 or True or on or yes or 1, all will be considered as true)
@app.get("/prod/{prod_id}")
async def read_item(prod_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": prod_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# ?------------------------------------------------------

# =>4
# Multiple path and query parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

# ?------------------------------------------------------

# =>5
# Required query parameters (just not declare any default value to make it required)
@app.get("/new_item/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item



################ REQUEST BODY ################
################ CORS ORIGINS ################
################ Databases ################



@app.get("/items/{item_id}", response_model=bool)
async def read_item(item_id: int):
    if item_id > 5:
        return False
    else:
        return True

# POST request


@app.post('/bool', response_model=bool)
async def read_bool():
    return True


@app.post('/items/', response_model=Item)
async def create_item(item: Item):
    return item


@app.put('/items/', response_model=Item)
async def update_item(item: Item):
    return item


@app.delete('/items/', response_model=Item)
async def delete_item(item: Item):
    return item


######### NOTES #########

'''
if you have same link with different type of data
then the first one will be counted, later one
will be ignored

@app.get("/items/{item_id}/{q}")
async def read_item(item_id: int, q: int):
    return {
        "item_id": item_id, "q": q
    }

confusing method age use korbo
'''

'''
@decorator Info

That @something syntax in Python is called a "decorator".

You put it on top of a function. Like a pretty decorative hat (I guess that's where the term came from).

A "decorator" takes the function below and does something with it.

In our case, this decorator tells FastAPI that the function below corresponds to the path / with an operation get.

It is the "path operation decorator".

'''
'''
1. Import FastAPI.
2. Create an app instance.
3. Write a path operation decorator (like @app.get("/")).
4. Write a path operation function (like def root(): ... above).
5. Run the development server (like uvicorn main:app --reload).
'''