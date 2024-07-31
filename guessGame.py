import random
import math

low = int(input("Enter the lower bound: "))
high = int(input("Enter the higher bound: "))

#Generating the random value
x = int(random.randint(low, high))

totalChances = int(math.log(high - low + 1, 2))
print("You get total", totalChances, "guesses to guess the number.")

count = 0
flag = False

while count < totalChances:
    count += 1
    guess = int(input("Enter a guess: "))

    if x == guess:
        print("Congratulations you did it in ", count, " try")
        flag = True
        break

    elif x > guess:
        print("You guessed too small!")
    else:
        print("You Guessed too high!")

if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")   