import random
import sys
import time

def setze_zeitstempel():

    return time.time() * 1000


def stelle_aufgabe():

    i = 0
    
    while True:

        i += 1
        print(" --- Aufgabe %d --- " % (i))
        rechne(0)

        
def rechne(mode = 0):

    answer_correct = False
    
    try:
        
        a = random.randint(0,9)
        b = random.randint(0,9)

        start = setze_zeitstempel()
        
        if mode == 0:
            print("%d x %d = ?" % (a, b))

            c = int(input())

            if (a * b) == c:
             56
             answer_correct = True

        elif mode == 1:
            print("%d + %d = ?" % (a, b))

            c = int(input())

            if (a + b) == c:
                answer_correct = True
                

        stop = setze_zeitstempel()
        
        if ((stop - start) < 5000) and answer_correct:
            print("Sehr gut")
        elif ((stop -start) < 10000) and ((stop - start) >= 5000) and answer_correct:
            print("Weiter so!")
        elif ((stop - start) >= 10000) and ((stop - start) < 15000) and answer_correct:
            print("Das geht doch schneller, oder?")
        elif ((stop - start) >= 15000 and answer_correct):
            print("Das war zu langsam")
        elif answer_correct is False:
            print("Antwort ist falsch")
        
    except ValueError as e:
        print("Falsche Eingabe")
        

if __name__ == "__main__":
    stelle_aufgabe()
