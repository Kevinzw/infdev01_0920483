print "welcome to Rock, Paper, Scissors"
def UserInput():
        Input = raw_input("Choose Rock(r). Paper(p) or Scissors (s) ")
         

        if not(Input == "r" or Input == "p" or Input == "s"):
            print "Fill in Rock(r), Paper(p) or Scissors(s)"
            return UserInput()
        return Input
u1 = UserInput()
u2 = UserInput()
       
    

winner = ""
if u1 == u2:
    winner = "It's a draw"
elif u1 == "r":
    if u2 == "p":
        winner = "Player 2 wins, paper covers rock"
    else:
        winner = "Player 1 wins, rock crushes scissors"
elif u1 == "p":
        if u2 == "r":
            winner = "Player 1 wins, paper cover rock"
        else:
            winner = "Player 2 wins, scissors cuts paper"    
elif u1 == "s":
        if u2 == "r":
            winner = "Player 2 wins, rock cruches scissors"
        else:
            winner = "Player 1 wins, scissors cuts paper"

            
print winner
