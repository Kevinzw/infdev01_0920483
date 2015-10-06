while True:
    import sys
    size = input("Enter an int: ")


    for i in range(size):
        for j in range (size):
            sys.stdout.write("*")
        print("")


