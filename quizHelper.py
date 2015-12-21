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
    
    if not file1 or os.path.isfile(file1)
        print "File does not exists"
        err()


    if definition and QA:
        QuizAll()
    elif definition:
        definition()
    elif QA:
        question()


if __name__ == "__main__":
    main(sys.argv[1:])
