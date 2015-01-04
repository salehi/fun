#!/bin/sh

# just for have some fun reviewing history :))

from random import randrange
from datetime import datetime

startTime = datetime.now()
answer = randrange(1, 1000)
is_correct = False

print("**** Guess What is the selected number ****\n")
input = raw_input("Options are between 0 and 1000 or press q to exit \n")
if input != "q":
    input = int(input)
    while is_correct == False:
        if input > answer:
            input = int(raw_input("the answer is smaller than this! Try again : "))
            continue
        elif input < answer:
            input = int(raw_input("the answer is bigger than this! Try again : "))
            continue
        else:
            print("*********************************************\n")
            print("************* Correct Answer ****************\n")
            print("*********************************************\n")
            is_correct = True
            continue

endTime = datetime.now()
diffTime = endTime - startTime
diffTime = diffTime.seconds

print("you have spend " + str(diffTime) + " second in this game! bye!")