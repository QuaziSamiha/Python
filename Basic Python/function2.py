# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter 
# name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# Arbitrary Arguments are often shortened to *args in Python documentations.


def family(*kids):
    print('The youngest child is : ', kids[2])

family('Sneha', 'Ahona', 'Ibrahim')

# Keyword Arguments
# You can also send arguments with the key = value syntax.
def children(c1, c2, c3):
    print('The youngest children is : ', c2)

children(c1='akku', c2='makku', c3='pakku')

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two 
# asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def name(**fullname):
    print('Samiha', fullname['lname'])

name(fname='Quazi', mname='Samiha', lname='Tasnim')

# Default Parameter Value


