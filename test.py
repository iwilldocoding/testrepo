#understanding what is type hints is 
'''age: int =25
def greet(name:str)->str:
    return f"hello,{name}"

print(result=greet(67))'''# now this will show type error since we previously defined what would the parameter type

# Optional types and collections

'''from typing import Optional, List ,Tuple

def get_user(id: int) -> Optional[str]:
    return None if id == 0 else " User"

print(result=get_user())'''


#now upto the pydantic library and understanding its use and BaseModel
'''from pydantic import BaseModel

class User(BaseModel):
    id:int
user=User(id="123")
print(user.id)
print(type(user.id))#this codes shows the pydantic capablity of data parsing and corecion
'''
#basic use of basemodel

from pydantic import BaseModel, Field , EmailStr
from typing import List, Optional 

'''class InventroyItem(BaseModel):
    name: str= Field(min_length=2, max_length=50)
    price: float=Field(gt=0, description ="the price must be greater than zero")
    quantity:int =Field(default=0, ge=0)
    tags: List[str] = []
try:
    item = InventroyItem(name="apple",price=89,quantity= "87")
    print(f"success item:{item.name} ,total value:item.price{item.price}")
    print(item.model_dump())
except Exception as e:
    print(f"validation failes:{e}")
    '''

'''from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()
class usercreate(BaseModel):
    username:str
    password: str
    age:int

@app.post("/register")
async def register_user(user: usercreate):
    if user.age<18:
        raise HTTPException(status_code=400, detail="User must be 18+")
    return {"message":f"User {user.username}"}'''
# now this the basic implementation of both async and pydantic in fastapi to build an end point so now lets start building a form section

