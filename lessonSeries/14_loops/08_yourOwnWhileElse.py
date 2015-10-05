from random import randint

guesses_left = 3
random_number = randint(1, 10)
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    guesses_left -= 1
else:
    print "You lose."
