while True:
    import sys
    size = int(input("Enter an int: "))

    for i in range(size):
        for j in range(size):
            if i == 0 or j == 0 or  i == size-1 or j == size-1:
                sys.stdout.write ("*")
            else:
                #stdout.write is the bomb, it just.. knows man
              sys.stdout.write(" ")
        print("")