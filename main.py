# le code ci-dessous contient des erreurs délibérées : identifiez-les et ajoutez des commentaires
# ensuite décommentez le bloc, corrigez puis exécutez et voyez qu'il s'exécute
number = int(input("Which number do you want to check?"))
# erreur courante pour comparer quelque chose dans une instruction if use "==" not "="
if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  






year = input("Which year do you want to check?")
# erreur courante où l'entrée est une chaîne et n'a pas été convertie en
# entier pour que les calculs puissent avoir lieu
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# erreur de logique - la ligne 32 doit être "et" et non "ou"
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])