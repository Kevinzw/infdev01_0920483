while True: 
    import sys
    size = input("Enter an int: ")



    for i in range(size):
        for j in range (i):
            if j == 0 or j == i-1 or i == size -1:
                sys.stdout.write("*")
            else:
                sys.stdout.write(" ")
        print("")


