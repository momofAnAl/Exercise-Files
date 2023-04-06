# build a program: the inpur string is palindrome 
def palindrome_function (teststr):
    #reverse the string by using slice strick
    if teststr == teststr[::-1]: 
        return True
    else:
        return False


run = True
while (run):
    teststr = input("Enter string to test for palindrome or 'exit':")

    #exit when the user type "exit":
    if teststr == "exit":
        run = False
        break
    # strip all the spaces and punctuation from the string
    newstr = ""
    for x in teststr:
        if x.isalnum():
            newstr += x

    print("Palindrome test:", palindrome_function(newstr))

# palindrome_function(teststr) 
                                                                                                                                                                                                                                 




