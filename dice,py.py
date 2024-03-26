import random

# print("die 1 =", random.randrange(1,6,1))
# print("die 3 =", int(random.random()*6+20))


# random dice role game
# ranNum = random.randint(1,6)
# guessNumber = -1
# count = 0

# while guessNumber != ranNum:
#     guess=input("What number do you think it will land on?")
#     guessNumber = int(guess)
#     count = count + 1
#     if guessNumber == ranNum:
#         print("You rolled a", ranNum)
#         print("you win")
#     else:
#         print("try again")
        

# if count == 1:
#     print("First try!!")
# else:
#     print("It took you" , count, "guesses")

#### for loops with and without the index 
# val = [25,26,27,28,29,30,31,32,33]
# for index , each in enumerate(["a", 'b', 'c', 'd', 'e']):
#     print (each, val[index])

# classroom = ['marcus', "andrew", "deasia"]
# for student in classroom:
#     print(student)


#### highest number in the list:

numbers = [3,42,12,9,74,15]
highest = 0


for number in numbers :
    if number > highest:
        highest = number
print(highest)