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


# print(bool("hello"))
# print(bool(""))
# print(bool("   "))
# print(bool(13))
# print(bool(0))
# print(bool([]))
# print(bool({}))
# print(bool(()))

# lists
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
mylist = ["name", "himanshu", "dube"]
print(mylist)
print(len(mylist))


list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))

'''There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.[]
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.()
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.{}
Dictionary is a collection which is ordered** and changeable. No duplicate members.{}
'''

first_list  = ["this", "is", "first", "list"]
second_list = ["second", 'list', "is", 'this']

first_list.append("thorin")
print(first_list)

first_list.insert(2, "gandalf")
print(first_list)

combined_list = first_list.extend(second_list) #None as it dosent work like this. 
print(combined_list) # This will be NONE. 

"""The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.)."""
first_list.extend(second_list)
print(first_list)

a =0
for x in first_list:
    print (f"index = {a} : value = {x}")
    a = a + 1


        # LIST COMPREHENSION 
"""List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list."""


old_list1 = ["mango", "apple", "strawberry", "muskmelon"]
new_list1 = []

for x in old_list1:
    if x == "apple":
        new_list1.append(f"wow_{x}")
    else:
        new_list1.append(x)

print(new_list1)

# newlist = [expression for item in iterable if condition == True]
new_list2 = [f"brilliant_{x}" for x in old_list1 if x == "apple"]
print(new_list2)
    
new_list3 = [x.upper() for x in old_list1]
print(new_list3)

new_list4 = [x.upper() if x == "apple" else x for x in old_list1]
print(new_list4)


#copying lists
copy_list = ['NEW', 'list', "going"]
final_list = copy_list

copy_list.append("copydone")
print(final_list)

unchnaged_list = copy_list.copy()

copy_list.append("foodEat")

print(unchnaged_list)

# join
print(old_list1 + copy_list)



##############TUPLES