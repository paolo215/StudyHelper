import getopt
import random
#-d = sheet for definitions
#-q = Q/A
#-a = all
#-o = quiz me using this file
a = open("ElemEthics.txt", "r")
string = a.read()
string = string.split("\n")
string = [f for f in string if string != ""]
length = len(string)
ignores = []
questions = int(raw_input("Enter how many questions: "))
for i in range(questions):
    rand = random.randint(0, length+1)
    while(rand in ignores):
        rand = random.randint(0, length+1)
    print string[rand], rand
    answer = raw_input("Answer: ")
    ignores.append(rand)
    print "\n"


