


def main():
    x = 0


    # define a while loop
    while (x < 5):
        print(x)
        x = x + 1 # x += 1


    # # define a for loop
    for x in range (5, 10):
        print(x)

    # use a for loop over while loop
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    # use the break and continue statements
    for x in range(5, 100):
        # if x == 7:
        #     break
        if x % 2 == 0:
            continue
        print(x)

    #using the enumerates to get index

    days = ["Mon", "Tue", "Wed","Thu","Fri","Sat","Sun"]
    for i,d in enumerate(days):
        print(i,d)

    
    # suing the enumerate() function to get back

main()

    