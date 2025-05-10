a= 5

print("a is 5") if a == 5 else print("a is not 5")


def counting(*name, **songs):
    print(type(name)) #tuple
    print(name)
    print(type(songs)) # dictionary
    print(songs)

counting("hello", "name", "himanshu", rehman="sawari", inder="arya")


############ CLASSES IN PYTHON ###########

"""All classes have a function called __init__(), which is always executed when the class is being initiated."""


class Person:
    def __init__(self, name:str, age:int):
        print(self, "self")
        self.name= name
        self.age = age

p1 = Person("ThorinOshield", 23)
print(p1)

"""The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:"""

class Person2:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    
    def __str__(self):
        return f"My name is {self.name} and age is {self.age}"
    
    """Object methods"""

    def call_my_name(self):
        return f"my name {self.name}, and I am wonderful"

p2 = Person2("ThorinOshield", 23)

print(p2.call_my_name())

"""The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:"""