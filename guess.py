import random

guessesTaken = 0

print('Hello! What is your name?')
myName = raw_input()

number = random.randint(1, 50)
print('Well, ' + myName + ', I want to play a game...')
print('I am thinking of a number between 1 and 50.')

while guessesTaken < 6:
	print('Take a guess')
	guess = raw_input()
	guess = int(guess)

	guessesTaken += 1

	if guess < number:
		print('Your guess is too low.')

	if guess > number:
		print('Your guess is too high.')

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken)
	print('Okay, ' + myName + ', you win this time...')
	print('Guesses Taken = ' + guessesTaken)

else:
	number = str(number)
	print('You failed. The number was ' + number + '. Watch your back...')
