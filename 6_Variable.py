######################################################################################################################
# Variables 👇
# A variable is a location in memory used to store same data(value).
# They are given unique names to differentiate between different memory locations. The rules for writing a variable name is same as the rules for writing identifiers in Python.
# We don’t need to declare a variable before using it. In Python, we simply assign a value to a variable and it will exist. We don’t even have a declare the type of the variable. This is handled internally according to the type of the value we assign to the variable.
# Variable Assignments 👇
# #We use the assignment operator (=) to assign values to a variable
######################################################################################################################
a = 10
b = 5.5
c = "Saheb"
# Multiple Assignments 👇
a , b , c = 10, 5.5, 'Saheb'
# Or
a = b = c = "AI"
# Storage Locations 👉
x = 3
print("Address of the variable x is {0}".format(id(x)))
y = 3
print("Address of the variable y is {0}".format(id(y)))
######################################################################################################################
# O/P:
# Address of the variable x is 1224656382320
# Address of the variable y is 1224656382320
# Observation:
# x and y points to same memory location.
######################################################################################################################

