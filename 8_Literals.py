######################################################################################################################
# Python Literals
# Literals are representations of fixed values in a program. They can be numbers, characters, or strings, etc.
# For example, 'Hello, World!', 12, 23.0, 'C', etc.
# Literals are often used to assign values to variables or constants. For example
# site_name = 'programiz.com'
# In the above expression, site_name is a variable, and 'programiz.com' is a literal.
######################################################################################################################
# Python Numeric Literals
# Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical
# types: Integer, Float, and Complex.
#
# Type	                Example	            Remarks
# Decimal	                5, 10, -68	        Regular numbers.
# Binary	                0b101, 0b11	        Start with 0b.
# Octal	                0o13	            Start with 0o.
# Hexadecimal	            0x13	            Start with 0x.
# Floating-point Literal	10.5, 3.14	        Containing floating decimal points.
# Complex Literal     	6 + 9j	            Numerals in the form a + bj, where a is real and b is imaginary part
######################################################################################################################
# Python Boolean Literals
# There are two boolean literals: True and False.
# For example,
# result1 = True
# Here, True is a boolean literal assigned to result1.
######################################################################################################################
# String and Character Literals in Python
# Character literals are unicode characters enclosed in a quote. For example,
# some_character = 'S'
# Here, S is a character literal assigned to some_character.
# Similarly, String literals are sequences of Characters enclosed in quotation marks.
# For example,
# some_string = 'Python is fun'
# Here, 'Python is fun' is a string literal assigned to some_string.
######################################################################################################################
# Special Literal in Python
# Python contains one special literal None. We use it to specify a null variable. For example,
#
# value = None
# print(value)
# # Output: None
#
# Here, we get None as an output as the value variable has no value assigned to it.
######################################################################################################################
# Literal Collections
# There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.
######################################################################################################################

# list literal
fruits = ["apple", "mango", "orange"]
print(fruits)

# tuple literal
numbers = (1, 2, 3)
print(numbers)

# dictionary literal
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
print(alphabets)

# set literal
vowels = {'a', 'e', 'i' , 'o', 'u'}
print(vowels)

######################################################################################################################
# Output
# ['apple', 'mango', 'orange']
# (1, 2, 3)
# {'a': 'apple', 'b': 'ball', 'c': 'cat'}
# {'e', 'a', 'o', 'i', 'u'}

# In the above example, we created a list of fruits, a tuple of numbers, a dictionary of alphabets having values with
# keys designated to each value and a set of vowels.
######################################################################################################################
