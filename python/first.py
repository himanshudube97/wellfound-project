# def greet(name):
#     return f"Hello, {name}"

# a = greet("himanshu")
# print(a)

# b = a

# print(id(b) == id(a))

# Closure

# def outerfunc(name):
#     lastname = "himanshu"
#     print(lastname)
#     def innerfunc():
#         value = f"my last name is {lastname}"
#         return value
    
#     innerfunc()

#     return f"outer {lastname}"

# outerfunc("brother")

#  decorator is like hoc

# def my_decorator(func):
#     def wrapper():
#         print("hello")
#         func()
#         print("bye")
    
#     return wrapper


# @my_decorator
# def say_hello():
#     print("great")

# say_hello()


# x = str(3)
# y = int('3')
# print(x)
# print(y)


# complexn = 2 + 5j
# print(complexn)

# str = "flauccinauccinihilification"
# for x in str:
#     print(x)

# print(len(str))

# if "uccl" in str : print("true") 
# print(str.upper())

# print(f"{str} in {int(34)} and going to be 577")


print(bool("hello"))
print(bool(""))
print(bool("   "))
print(bool(13))
print(bool(0))
print(bool([]))
print(bool({}))
print(bool(()))
