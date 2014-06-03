from __future__ import print_function
def older_code(): 
  count = 1
  while count <= 5:
    print(count)
    count +=1

  while True:
    # Python 3 uses input, rather than raw_input, although raw_input also
    # works in Python 3, apparently
    stuff = raw_input("String to capitalize [type q to quit]: ")
    if stuff == "q":
      break
    print(stuff.capitalize())

  while True:
    value = raw_input("Integer, please [q to quit]: ")
    if value == 'q':      # quit
      break
    number = int(value)
    if number % 2 == 0:   # an even number
      continue
    print(number, "squared is", number*number)

  # An example of how to use an else clause with a while
  numbers = [1, 3, 5, 7]
  position = 0
  while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
      print('Found even number', number)
      break
    position += 1
  else:  # break not called
    print('No even number found')

  # Iterate over a collection
  rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
  current = 0
  while current < len(rabbits):
    print(rabbits[current])
    current += 1

  # A more Pythonic way to do the above
  for rabbit in rabbits:
    print(rabbit)

  # Iterate over string
  word = 'cat'
  for letter in word:
    print(letter)

# Iterate over a dictionary (Gives the keys)
accusation = {
  'room': 'ballroom',
  'weapon': 'lead pipe',
  'person': 'Colonel Mustard',
}

for card in accusation: # same as for card in accusation.keys():
  print(card)

# Gets the values
for value in accusation.values():
  print(value)

# Gets key and value as a tuple
for item in accusation.items():
  print(item)

# Assigning to a tuple in one step
for card, contents in accusation.items():
  print('Card', card, 'has the contents', contents)
