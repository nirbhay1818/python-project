
import math
import random

ll = int(input("Enter lower limit of number="))
ul = int(input("Enter upper limit of number="))
##random number
num = random.randint(ll,ul)
##number of attempts
count = round(math.log(ul - ll + 1, 2))
print("You have {} attempts ".format(count))
i = 0
while i < count:
        i += 1
        ## Taking input Of guessed number by user
        num1 = int(input("Enter your guess="))
        ## check whether guessed number is right or not
        if num1 == num:
            print(" you guessed the right number")
            break

        elif num1 < num:
                print("the guessed number is too less ")
        elif num1 > num:
                print("the guessed number is too large ")

        ## message for failed attempt
        if i >= count:
            print("\nmaximum attempts limit reached")
            print("\nbetter luck next time!!")
            print("the right number is ",num)
print("\n***Thank You***")
