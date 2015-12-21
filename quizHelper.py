import getopt
import random
import sys
#-d = sheet for definitions
#-q = Q/A
#-a = all
#-o = quiz me using this file



def usage():
    print """Commands:
    -d definition quiz
    -q questions and answers quiz
    -a all
    -i input file
    """

def err():
    usage()
    sys.exit()

def main(argv):


    definition = False
    QA = False
    
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

    if definition and QA:
        QuizAll()
    elif definition:
        definition()
    elif QA:
        question()


if __name__ == "__main__":
    main(sys.argv[1:])
