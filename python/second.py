# Tuples
"""A tuple is a collection which is ordered and unchangeable."""

my_tuple = ("apple", "mango", "banana", "apple")
print(my_tuple)


one_item = ("kiwi")
print(type(one_item)) # str

two_item =("pomegrante",)
print(type(two_item)) #tuple


"""Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple."""

test_tuple = ("himanshu", "pradeep", "manish", "kapil")
converted_list = list(test_tuple)
converted_list[2] = "kala"
final_tuple = tuple(converted_list)
print(converted_list)



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

"""UNPACKING A TUPLE"""
(green, *red , yellow) = fruits  #this is kind of destructuring we do in js
print(green)
print(red)
print(yellow)

"""ONLY TWO FUNCTIONS ARE AVAILABLE FOR TUPLE   a) count and b) index """