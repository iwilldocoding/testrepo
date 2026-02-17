from pydantic import BaseModel,  ConfigDict

class User(BaseModel):
    id: int
    name: str ='Jane Doe'
    model_config = ConfigDict(str_max_length=10)

user = User(id='124')#user is an instance of the User model
user2 = User(id='125',name='hello')



print(user2.name, user2.id)