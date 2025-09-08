from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True

user_data = {
    'id': "one",
    'username': "name",
    'email': "sss@ddf.com"
    }

user = User(**user_data)
print(user.is_active)
print(user.id )