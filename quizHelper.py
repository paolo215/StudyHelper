import getopt
import random
import sys
import os
#-d = sheet for definitions
#-q = Q/A
#-a = all
#-o = quiz me using this file



def usage():
    print """Commands:
    -d definition quiz (format: word:definition)
    -q questions and answers quiz (format: question)
    -a all
    -i input file
    """

def err():
    usage()
    sys.exit()



def definition(string):
    string = string.split("\n")
    string = [f.split(":") for f in string]
    try:
        num = int(raw_input("Enter how many questions: "))
    except ValueError:
        print "Invalid input. Please enter a number"
        sys.exit()

    switch = 0 #0 define the word
                #1 what is it
    length = len(string)
    for i in range(num):
        switch = random.randint(0, 1)
        question = random.randint(0, length)
        question = string[question]
        if switch == 0:
            print "Define: {}".format(question[0])
        else:
            print "{}".format(question[1])
        answer = raw_input("Answer: ")


def main(argv):
    definition = False
    QA = False
    file1 = ""
    
    try:
        opts, args = getopt.getopt(argv, "dqai", ["definition", "questions", "all", "input"])
    except getopt.GetoptError:
        err()

    for opt, arg in opts:
        if opt == "-h":
            err()
        elif opt in ("-d", "--definition"):
            definition = True
        elif opt in ("-q", "--questions"):
            QA = True
        elif opt in ("-a", "--all"):
            definition = True
            QA = True
        else:
            err()
    
    if not file1 or os.path.isfile(file1):
        print "File does not exists"
        err()

    file1 = open(file1, "r")
    string = file1.read()
    file1.close()
    if definition and QA:
        quizAll(string)
    elif definition:
        definition(string)
    elif QA:
        question(string)


if __name__ == "__main__":
    main(sys.argv[1:])
