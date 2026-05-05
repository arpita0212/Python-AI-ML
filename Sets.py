thisset = {"apple", "banana", "cherry"}
# print(thisset)

# Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

thisset = {"apple", "banana", "cherry", False, 0, 2}
# print(thisset)

# Get the Length of a Set
thisset = {"apple", "banana", "cherry"}
# print(len(thisset))

# Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}
# print(set1)

# type()

myset = {"apple", "banana", "cherry"}
# print(type(myset))

# set() constructor
thisset = set(("apple", "banana", "cherry"))
# print(thisset)

# Python - Access Set Items
thisset = {"apple", "banana", 'cherry'}
for x in thisset:
    # print(x)

# Check if "banana" is present in the set:
# thisset = {"apple", "banana", "cherry"}
# print("banana" in thisset) #True

# Check if "banana" is NOT present in the set:
 thisset = {"apple", "banana", "cherry"}
#  print("banana" not in thisset)

# once a set is created we cannot change its items, but you can add new items

# add set items
 thisSet = {"apple", "banana", "cherry"}
 thisSet.add("orange")

# print(thisSet)

# add sets

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
# print(thisset)

# add any iterable

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
# print(thisset)

# Python - Remove Set Items

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
# Note: If the item to remove does not exist, remove() will raise an error.
print(thisset)

# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
# Note: If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.

# The return value of the pop() method is the removed item.

# Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()

print(x)
# print(thisset)

# The clear() method empties the set:

thisset.clear()
# print(thisset)

# The del keyword will delete the set completely:

del thisset
# print(thisset)

#  print(thisset)          ^^^^^^^
# NameError: name 'thisset' is not defined. Did you mean: 'thisSet'?

# Loop Sets

#  thisset = {"apple", "banana", "cherry"}
#  for x in thisset:
#      print(x)



# Joins Set

# 1) The union() and update() methods joins all items from both sets
# 2) intersection() method keeps Only the duplicates
# 3) the difference() method keeps the items from the first set that are not in the other sets
# 4) the symmetric difference() methods keeps all items except the duplicates


# union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# we can use | operator instead of union and we will get the same result

set4 = set1 | set2
print(set4)

# Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# frozenset is an immutable version of a set.

# Like sets, it contains unique, unordered, unchangeable elements.

# Unlike sets, elements cannot be added or removed from a frozenset.

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
