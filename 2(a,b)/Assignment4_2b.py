print "welcome to Rock, Paper, Scissors, Lizard, Spock"
def UserInput():
        Input = raw_input("Choose Rock(r). Paper(p), Scissors (s), Lizard(l) or Spock(sp) ")
         
        if not(Input == "r" or Input == "p" or Input == "s" or Input == "l" or Input == "sp"):
            print "Fill in Rock(r), Paper(p), Scissors(s), Lizard(l) or Spock(sp)"
            return UserInput()
        return Input
u1 = UserInput()
u2 = UserInput()
       
    

winner = ""
if u1 == u2:
    winner = "It's a draw"
elif u1 == "r":
        if u2 == "p":
            winner = "Player 2 wins, paper cover rock"
        elif u2 == "s":
            winner = "Player 1 wins, rock cruches scissors"
        elif u2 == "l":
            winner = "Player 1 wins, rock crushes lizard"
        elif u2 == "sp":
            winner = "Player 2 wins, spock vaporizes rock"
elif u1 == "p":
        if u2 == "r":
            winner = "Player 1 wins, paper cover rock"
        elif u2 == "s":
            winner = "Player 2 wins, scissors cut paper"
        elif u2 == "l":
            winner = "Player 2 wins, lizard eats paper"
        elif u2 == "sp":
            winner = "Player 1 wins, paper disproves spock"
elif u1 == "s":
        if u2 == "r":
            winner = "Player 2 wins, rock cruches scissors"
        elif u2 == "p":
            winner = "Player 1 wins, scissors cut paper"
        elif u2 == "l":
            winner = "Player 1 wins, scissors decapitates lizard"
        elif u2 == "sp":
            winner = "Player 2 wins, spock smashes scissors"
elif u1 == "l":
        if u2 == "r":
            winner = "Player 2 wins, rock crushes lizard"
        elif u2 == "p":
            winner = "Player 1 wins, lizard eats paper"
        elif u2 == "s":
            winner = "Player 2 wins, scissors decapitates lizard"
        elif u2 == "sp":
            winner = "Player 1 wins, lizard poisons spock"
elif u1 == "sp":
        if u2 == "r":
            winner = "Player 1 wins, spock vaporizes rock"
        elif u2 == "p":
            winner = "Player 2 wins, paper disproves spock"
        elif u2 == "s":
            winner = "Player 1 wins, spock smashes scissors"
        elif u2 == "l":
            winner = "Player 2 wins, lizard poisons spock"
print winner
            

