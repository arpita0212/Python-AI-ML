mytuple = ("apple", "banana", "cherry")

# print tuple
# print(mytuple)

#  allow duplicates

DuplicateTuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(DuplicateTuple)

# length

# print(len(DuplicateTuple))


# Create Tuple With One Item

thisTuple = ("apple",)
# print(type(thisTuple))  # this is a tuple

thisNotTuple = ("apple")
# print(type(thisNotTuple))# this is a string 

# tuple constructor

thisTuple1 = tuple(("apple", "banana", "cherry"))
# print(type(thisTuple1))


# access tuple items
thisTupleAccess = ("apple", "banana", "cherry")
# print(thisTupleAccess[1])

# negative indexing
thisTupleNegative = ("apple", "banana", "cherry")
# print(thisTupleNegative[-1])

# range indexes
thisTupleRangeIndexes = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thisTupleRangeIndexes[2:5])


# updating
# Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# print(x)

# add items

AddingTuple = ("apple", "banana", "cherry")
y = list(AddingTuple)
y.append("orange")
AddingTuple = tuple(y)


# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.append("orange")
thisTuple = tuple(y)

# Add tuple to a tuple

thisTuple = ("apple", "banana", "cherry")
y = ("orange",)
thisTuple += y 
# print(thisTuple)

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thisTuple = ("apple", "banana", "cherry")
y = list(thisTuple)
y.remove("apple")
thisTuple = tuple(y)

# delete the tuple completely
thisTuples = ("apple", "banana", "cherry")
del thisTuples
# print(thisTuples) #this will raise an error because the tuple no longer exists


# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
# print(thistuple)

# Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)


# Add a list of values the "tropic" variable:

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)


# Loop Tuples
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    # print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])


thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1


# Join Tuples

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
ptint(tuple3)

# multiply tuple

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# tuple methods
