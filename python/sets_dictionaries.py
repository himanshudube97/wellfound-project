"""Set items are unordered, unchangeable, and do not allow duplicate values."""

test_set = {"name", "himanshu", "greatness"}
print(test_set)

unique_check = {"name", 1, True, "himanshu", "himanshu", "name"}  
print(unique_check)  #{1, 'name', 'himanshu'} result as 1 and true are considered as same. 



# ######  DICTIONARIES


my_dict = {
    "name": 'himanshu',
    "age": 28,
    "area": "Garur"
}

print(my_dict["age"])
# print(my_dict["hello"])
print(my_dict.get("hello")) # Result is NONE better then error from above. 
print(my_dict.keys())
print(my_dict.values())

my_dict["add"] = "new_element"
print(my_dict)

my_dict.update({"color": "red"})
print(my_dict)

for x in my_dict:
    print(f'The value {x} is {my_dict[x]}')



""". Unpacking a Dictionary
If you already have a dictionary:"""

data = {"name": "Alice", "age": 30}

def greet(name, age):
    print(f"Hello {name}, age {age}")

greet(**data)  # Unpacks name and age into the function arguments
"""
2. Unpacking a Pydantic Object or Class
If you have a custom object (like a Pydantic model or class), you must first convert it to a dict-like form."""


from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Bob", age=25)

print(user.dict())   # {'name': 'Bob', 'age': 25}
greet(**user.dict()) # Unpack and pass to function



# data = {"names": "himanshu", "age": 50, "class": "eight"}
# la = {"hello": "greet", "bro": "yes"}
# print({**data, **la})