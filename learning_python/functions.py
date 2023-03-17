


# define BASIC function:
def func1():
    print("I am a function")

#function that takes arguments:
def func2(arg1, arg2):
    print(arg1," ", arg2)

# function that returns a value
def cube(x):
    return x * x * x

#function with default value for an arguement
# def power(num, x=1):
#     result = 1;
#     for i in range (x):#x=3 so the loop go 3 times
#         result = result * num
#     return result

# print(power(2))
# print(power(2,3))

# print(power(x=3, num=2))

#function with variable number of arguments
def muilti_add(n = 1, *args): # *: list have no input
    result = 0
    for x in args:
        result += x
    return n, result

print (muilti_add(4,5,7,8, 10))





# func1()
# print(func1())
# print(func1)

# func2(8, 10)
# print(func2(8, 10))

# cube(5)
# print(cube(5))

#

