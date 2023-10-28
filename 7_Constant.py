######################################################################################################################
# Python Constants
# A constant is a special type of variable whose value cannot be changed.
# In Python, constants are usually declared and assigned in a module (a new file containing variables, functions, etc which
# is imported to the another file where constant will be used).
######################################################################################################################
# import constant file we created above
import constant_container
print(constant_container.PI) # prints 3.14
print(constant_container.GRAVITY) # prints 9.8
######################################################################################################################
# In the above example, we created the constant_container.py module file. Then, we assigned the constant value to PI and GRAVITY.
# After that, we create the constant.py file and import the constant_container module. Finally, we printed the constant value.
######################################################################################################################
# Note: In reality, we don't use constants in Python. Naming them in all capital letters is a convention to separate them
# from variables, however, it does not actually prevent reassignment.
######################################################################################################################


