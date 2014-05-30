# This is a guess the number game.
# IMPROVEMENT

# Suggested by Daddy
# 1. Program asks you how many goes you want.
# 2. Random insult instead of just 'dimwit'

# Suggested by Thomas
# 1. Stop it crashing when you put a letter in

# Completed by Thomas
# 1. Say "Eh up, Hello".


import random

guessesTaken = 0
insults = "dimwit idiot silly-billy dunce mushy-brain bimble-bomble split-coat fishface fish-stone stinky-bum".split();

print('Hello! What are you called?')
myName = input()

number = random.randint(1, 20)
print('Eh up, Hello ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
  print('Take a guess.') # There are two spaces in front of print.
  guess = input()
  guess = int(guess)
  if guess < 0 or guess > 20:
    insult = random.randint(0, len(insults)-1)
    print('That\'s not between 1 and 20, ' + insults[insult] + '!');
    
  else:
    guessesTaken = guessesTaken + 1

    if guess < number:
      print('HIGHER!.') # There are four spaces in front of print.

    if guess > number:
      print('LOWER!!.')

    if guess == number:
      break

if guess == number:
  guessesTaken = str(guessesTaken)
  print('Fabulous, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses! You are way too clever.')

if guess != number:
  number = str(number)
  print('You got it all wrong - silly billy!. The number I was thinking of was ' + number)
