######################################################################################################################
# Python Keywords
# Keywords are predefined, reserved words used in Python programming that have special meanings to the compiler.
#
# We cannot use a keyword as a variable name, function name, or any other identifier. They are used to define the
# syntax and structure of the Python language.
######################################################################################################################
import keyword
print(keyword.kwlist)
print("\nTotal number of keywords: ", len(keyword.kwlist))
######################################################################################################################
# OUTPUT:
# ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#
# Total number of keywords:  36
######################################################################################################################
# Identifier is the name given to entities like class, functions, variables etc. in python . It helps differentiating one
# entity from another.
# Rules for writing Identifiers:
#     Identifiers cannot be a keyword.
#     Identifiers are case - sensitive.
#     It can have a sequence of letters and digits.However, it must begin with a letter or _.The first letter of an
#     identifier cannot be a digit.
#     It's a convention to start an identifier with a letter rather _. Whitespaces are not allowed.
#     We cannot use special symbols like !, @, #, $, and so on.
######################################################################################################################
######################################################################################################################
