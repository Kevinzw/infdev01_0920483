input = raw_input("Please enter a sentence that you want to reverse:\n")
console = ""
IntNumber = 0
while IntNumber < len(input):
    console = input[IntNumber] + console
    IntNumber+=1
print console