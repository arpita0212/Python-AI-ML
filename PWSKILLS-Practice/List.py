myList = ["apple", "banana", "cherry"]

#  print the list
# print(myList)

#  allow duplicates

thisList = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thisList)

# print(len(thisList))  # length of the list

# can contain different data types
list1 = ["abc", 34, True, 40, "female"]
# print(list1)

# find the data type
myList1 = ["apple", "banana", "cherry"]
# print(type(myList1))

#list constructor
thisList1 = list(("apple", "banana", "cherry")) # double round-brackets
# print(thisList1)

#  print second item of the list

accessList = ["apple", "banana", "cherry"]
# print(accessList[1])


# negative indexing ->  print the last item of the list
thisList2 = ["apple", "banana", "cherry", "grapes"]
# print(thisList2[-1])

# range of indexes -> return the third, fourth, and fifth item
thisLists = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thisLists[3:6])

# This example returns the items from the beginning to, but NOT including, "kiwi":

thislistNotIncluded = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislistNotIncluded[:4])

# This example returns the items from "cherry" to the end:
thislistss = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislistss[2:])



# Range of Negative Indexes
thislistNegativeIndex = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislistNegativeIndex[-4:-1])

# Check if Item Exists
thislistCheck = ["apple", "banana", "cherry"]
if "apple" in thislistCheck:
    print('Yes, apple is in the fruits list')