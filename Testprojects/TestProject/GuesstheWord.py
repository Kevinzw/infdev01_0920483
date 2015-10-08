import random

#open words.txt as a wordlist for the AI
with open ('words.txt', 'r'):  infile_name = 'words.txt'

def chooseword(infile_name):
    infile = open(infile_name, 'r')
    wordlist = infile.readlines()
    total_words = len(wordlist)
    random_num = random.randint(0, total_words -1)

    chosen_word = wordlist[random_num].replace('\n', '')
    word_len = len(chosen_word)
    return chosen_word, word_len

    
    
    
def main(win, infile_name):
    word, word_len = chooseword(infile_name)
    grid = '__'
    for i in range(word_len - 1):
        grid - grid + ' __'
        
    strikes = 0
    guessed_letters = []
    wordguess = False

    while strikes < 7 and wordguess == False:
        guess = input("Enter a single letter: ")
        if guess == ' ' or guess == '' or len(guess) != 1:
            print "Please enter a single letter. Try again fucktard"
        continue

            
        if guess in word.lower() and not(guess in guessed_letters):
            guessed_letters.append(guess)
            grid = word
            for letter in word:
                if (not (letter.lower() in word) or not (letter.lower() in guessed_letters)) and letter != ' ':
                    grid = grid.replace(letter, ' __ ')

    
main (False, False)

    

       