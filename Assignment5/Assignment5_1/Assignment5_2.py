while True:
    input = raw_input("Enter password:\n")
    points = 0
    passwordstr = ""
 

    if len(input) <= 6:
        points += 5
    elif len(input) <= 10:
        points += 10
    elif len(input) >= 13:
        points += 20

    for char in input:
        if char.islower():
            points += 2
        elif char.isdigit():
            points += 3
        elif char.isupper():
            points += 3
        else:
            points += 5

    if points >= 5 and points <= 20:
        passwordstr = "weak"
    elif points >= 25 and points <= 40:
        passwordstr = "medium"
    else: 
        passwordstr = "strong"

            

    print "you're password is worth", points, "points and is classified as", passwordstr, "\n"
