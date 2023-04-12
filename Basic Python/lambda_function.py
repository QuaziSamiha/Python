# --------------------------------- lambda function --------------------
function_name = lambda x, y, z: x + y * z
print(function_name(2, 4, 5))

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda a,b: (a+b)/2
print(double(4))
print(cube(5))
print(avg(3, 5))

# --------- passing lambda function as a function argument ---------------------
def function2(func, value):
    return 6 + func(value)

print(function2(double, 4))
print(function2(lambda w: w * w, 5))

# ------------------ lambda function within a function -------------------------
def myFunction (a):
    return lambda n: a * n

number_doubler = myFunction(2)
number_tripler = myFunction(3)

print(number_doubler(11))
print(number_tripler(11))