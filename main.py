import random
awnser = int()
number = random.randrange(10)

while awnser != number:
  try:
    awnser = int(input("Voer een nummer in:"))
  except:
    awnser  = int(input("Dat was geen nummber.\nVoer een nummer in:"))

print("You guessed it!")