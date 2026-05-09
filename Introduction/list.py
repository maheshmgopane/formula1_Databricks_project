#what is list in python
#list is a collection of items which is ordered and changeable. It allows duplicate members.  
# Lists are written with square brackets [] and items are separated by commas.
# Lists can contain items of different data types, including integers, strings, floats, and even other lists.
# Lists are mutable, which means you can change their content without changing their identity. You can add, remove, or modify items in a list after it has been created.
# Lists are ordered, which means that the items have a defined order, and that order will not change unless you explicitly modify it. You can access items in a list by their index, which starts at 0 for the first item.
# Lists are a versatile data structure in Python and are commonly used for storing and manipulating collections of data. They provide various built-in methods for adding, removing, and modifying items, as well as for sorting and searching through the list.
#   ways to create a list in python
#1. Using square brackets []
my_list = [1, 2, 3, 4, 5]   
print(my_list)    #output: [1, 2, 3, 4, 5]
#2. Using the list() constructor
my_list = list((1, 2, 3, 4, 5))
print(my_list)    #output: [1, 2, 3, 4, 5]
#3. Using list comprehension
my_list = [x for x in range(1, 6)]
print(my_list)    #output: [1, 2, 3, 4, 5]
#4. Using the split() method
my_string = "1,2,3,4,5"
my_list = my_string.split(",")
print(my_list)    #output: ['1', '2', '3', '4', '5']
#5. Using the range() function
my_list = list(range(1, 6))
print(my_list)    #output: [1, 2, 3, 4, 5]
#6. Using the list() constructor with a string
my_string = "Hello"
my_list = list(my_string)   
print(my_list)    #output: ['H', 'e', 'l', 'l', 'o']
#7. Using the list() constructor with a tuple
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)    #output: [1, 2, 3, 4, 5]
#8. Using the list() constructor with a set
my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
print(my_list)    #output: [1, 2, 3, 4, 5]
#9. Using the list() constructor with a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
my_list = list(my_dict)
print(my_list)    #output: ['a', 'b', 'c']
#10. Using the list() constructor with a range of numbers
my_list = list(range(1, 6))
print(my_list)    #output: [1, 2, 3, 4, 5]
#11. Using the list() constructor with a string and a separator
my_string = "Hello,World,Python"    
my_list = my_string.split(",")
print(my_list)    #output: ['Hello', 'World', 'Python']

#list indexing and slicing
#indexing is the process of accessing individual items in a list using their position or index. In Python, list indexing starts at 0, which means that the first item in a list is accessed using index 0, the second item is accessed using index 1, and so on. You can also use negative indexing to access items from the end of the list, where -1 refers to the last item, -2 refers to the second-to-last item, and so on.
lst= [1, 2, 3, 4, 5]
print(lst[0])    #output: 1
print(lst[1])    #output: 2
print(lst[2])    #output: 3     
print(lst[3])    #output: 4
print(lst[4])    #output: 5
print(lst[-1])    #output: 5
print(lst[-2])    #output: 4
print(lst[-3])    #output: 3
print(lst[-4])    #output: 2
print(lst[-5])    #output: 1

lst=list.append(6)    #appending an item to the end of the list
print(lst)    #output: [1, 2, 3, 4, 5, 6]
lst[0:3] = [7, 8, 9]    #modifying a slice of the list
print(lst)    #output: [7, 8, 9, 4, 5, 6]
lst2 = [10, 11, 12]
lst.extend(lst2)    #extending the list with another list   
print(lst)    #output: [7, 8, 9, 4, 5, 6, 10, 11, 12]
lst=lst+lst2    #concatenating two lists
print(lst)    #output: [7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12]
print(lst*2)    #repeating the list
#output: [7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12, 7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12]
#membership testing
print(7 in lst)    #output: True
print(13 in lst)    #output: False
print(7 not in lst)    #output: False
print(13 not in lst)    #output: True
#aliasing and copying a list
lst2 = lst    #creating a new reference to the same list
print(lst2)    #output: [7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12]
lst2.append(13)    #modifying the list through the new reference
print(lst)    #output: [7, 8, 9, 4,5, 6, 10, 11, 12, 10, 11, 12, 13]
print(lst2)    #output: [7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12, 13]
lst3 = lst.copy()    #creating a copy of the list
print(lst3)    #output: [7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12, 13]
lst3.append(14)    #modifying the copy of the list
print(lst)    #output: [7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12, 13]
print(lst3)    #output: [7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12, 13, 14]
lst.append(15)    #appending an item to the end of the list
print(lst)    #output: [7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12, 13, 15]
lst.extend([16, 17, 18])    #extending the list with another list
print(lst)    #output: [7, 8, 9, 4, 5, 6, 10, 11, 12, 10, 11, 12, 13, 15, 16, 17, 18]
lst.insert(0, 0)    #inserting an item at a specific index
print(lst)    #output: [0, 1, 2, 3, 4, 5, 6]
lst.insert(3, 'Hi')    #inserting an item at a specific index
print(lst)    #output: [0, 1, 2, 'Hi', 3, 4, 5, 6]
lst.remove(3)    #removing an item from the list
print(lst)    #output: [0, 1, 2, 'Hi', 4, 5, 6] 
lst.pop()    #removing the last item from the list
print(lst)    #output: [0, 1, 2, 4, 5]
lst.pop(4)    #removing an item at a specific index
print(lst)    #output: [1, 2, 4, 5]
lst.clear()    #removing all items from the list
print(lst)    #output: []   
lst = [1, 2, 3, 4, 5]
lst.index(3)    #finding the index of an item in the list
print(lst.index(3))    #output: 2
del lst[0]    #deleting an item at a specific index
print(lst)    #output: [2, 3, 4, 5]
del lst    #deleting the entire list
# print(lst)    #output: NameError: name 'lst' is not defined
#list counting and sorting
lst = [1, 2, 3, 4, 5, 3, 2, 1]
print(lst.count(3))    #output: 2
print(lst.count(2))    #output: 2
#sorting a list
lst = [5, 2, 9, 1, 5, 6]
lst.sort()    #sorting the list in ascending order
print(lst)    #output: [1, 2, 5, 5, 6, 9]
lst.sort(reverse=True)    #sorting the list in descending order
print(lst)    #output: [9, 6, 5, 5, 2, 1]
#sorting a list using the sorted() function
lst = [5, 2, 9, 1, 5, 6]
sorted_lst = sorted(lst)    #sorting the list in ascending order
print(sorted_lst)    #output: [1, 2, 5, 5, 6, 9]
sorted_lst = sorted(lst, reverse=True)    #sorting the list in descending order
print(sorted_lst)    #output: [9, 6, 5, 5, 2, 1]
#reversing a list
lst = [1, 2, 3, 4, 5]
lst.reverse()    #reversing the list
print(lst)    #output: [5, 4, 3, 2, 1]
lst = [1, 2, 3, 4, 5]   
reversed_lst = reversed(lst)    #reversing the list using the reversed() function
print(list(reversed_lst))    #output: [5, 4, 3, 2, 1]
#finding list values minimum and maximum
lst = [1, 2, 3, 4, 5]
print(min(lst))    #output: 1
print(max(lst))    #output: 5

lst = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]
s3=lst.intwersect(lst2)    #finding the intersection of two lists
print(s3)    #output: []

#nested lists
nested_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_lst)    #output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_lst[0])    #output: [1, 2, 3]
print(nested_lst[1])    #output: [4, 5, 6]
print(nested_lst[2])    #output: [7, 8, 9]
print(nested_lst[0][0])    #output: 1
print(nested_lst[0][1])    #output: 2
print(nested_lst[0][2])    #output: 3

#list comprehension
mynum=list(range(1, 6))
print(mynum)    #output: [1, 2, 3, 4, 5]

lst=[x**2 for x in range(1, 6)if x % 2 == 0]
print(lst)    #output: [4, 16]


squares = [x**2 for x in range(1, 6)]
print(squares)    #output: [1, 4, 9, 16, 25]
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)    #output: [2, 4, 6, 8, 10]
#membership testing


lst = [1, 2, 3, 4, 5]   
print(3 in lst)    #output: True
#creating a list
my_list = [1, 2, 3, 4, 5]   
print(my_list)    #output: [1, 2, 3, 4, 5]
#creating a list with different data types  
my_list = [1, "Hello", 3.14, True]
print(my_list)    #output: [1, 'Hello', 3.14, True]
#accessing list items
my_list = [1, 2, 3, 4, 5]   
print(my_list[0])    #output: 1
print(my_list[1])    #output: 2
print(my_list[2])    #output: 3
print(my_list[3])    #output: 4
print(my_list[4])    #output: 5
#negative indexing
my_list = [1, 2, 3, 4, 5]
print(my_list[-1])    #output: 5
print(my_list[-2])    #output: 4    
print(my_list[-3])    #output: 3
print(my_list[-4])    #output: 2
print(my_list[-5])    #output: 1
#slicing a list
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])    #output: [2, 3, 4]
print(my_list[:3])    #output: [1, 2, 3]
print(my_list[2:])    #output: [3, 4, 5]
print(my_list[:])    #output: [1, 2, 3, 4, 5]

