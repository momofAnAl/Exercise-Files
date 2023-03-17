myint = 5
myfloat = 13.2
mystr = "This is string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

# print(myint)
# print(myfloat)
# print(mystr)
# print(mybool)
# print(mylist)
# print(mytuple)
# print(mydict)

# #sequence type, use []
# print(mylist[2])
# print(mytuple[1])

# # to slice to get part of sequence
# print(mylist[1:5])
# print(mylist[2:4:2])

#use slices [] to reverse the sequence
# print(mylist[::-3])

#dictionaries are accssed via keys
# print(mydict["one"])

# #Error: variables of different types cannot be combined
# print("abc" + str(123))

#global vs. local variables in functions
def somefucntion():
    global mystr
    mystr = "I love you"
    print(mystr)

somefucntion()
print(mystr)

del mystr
print(mystr)

