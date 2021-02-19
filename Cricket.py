import random
num = [1,2,3,4,5,6]
rand = -1
runs = 0
score = 0
tossopt = 0
tossvar=[1,2]
flags = 1
def exit():
    while True:
        break
print('Toss')
print('1->Heads 2->Tails')
toss = int(input())
if (toss == random.choice(tossvar)):
  print("You won the toss!")
  print("What would you like to do??")
  print('1->Batting 2->Bowling ')
  tossopt = int(input())
  if (tossopt == 1):
    print("Its your turn to bat!!")
    while (runs!=rand):
      runs = int(input('Enter the run '))
      if (0<runs<=6):
        rand = random.choice(num)
        print(rand)
        if (runs == rand):
          print("Out!!")
          print("Its your turn to bowl now!")
          print("Your final score is",score)
          print("Opponent needs",score+1,"runs to win!")
        else:
          score = score + runs
          print("Your current score is",score)
      else:
        print("Enter run less than or equal to 6")
    total=0
    while (total<=score):
      runs=int(input('Enter the run '))
      if (0<runs<=6):
        rand = random.choice(num)
        print(rand)
        if (runs == rand):
          print("Out!!")
          print("You won and opponent lost by",(score-total),"runs!")
          print("Opponent's final score is",total)
          exit()
        else:
          total = total + rand
          print("Opponent's current score is",total)
      else: 
        print("Enter run less than or equal to 6")
    else:
      print("You lost and the opponent won because the opponent chased down the target successfully!")
  if (tossopt == 2):
    print("Its your turn to bowl!!")
    score = 0
    while (runs!=rand):
      runs = int(input('Enter the run '))
      if (0<runs<=6):
        rand = random.choice(num)
        print(rand)
        if (runs == rand):
          print("Out!!")
          print("Its your turn to bat now!")
          print("Opponent's final score is",score)
          print("You need",score+1,"runs to win!")
        else:
          score = score + rand
          print("Opponent's current score is",score)
      else: 
        print("Enter run less than or equal to 6")
    total=0
    while (total<=score):
      runs = int(input('Enter the run '))
      if (0<runs<=6):
        rand = random.choice(num)
        print(rand)
        if (runs == rand):
          print("Out!!")
          print("You lost and opponent won by",(score-total),"runs!")
          print("Your final score is",total)
          exit()
        else:
          total = total + runs
          print("Your current score is",total)
      else:
        print("Enter run less than or equal to 6")
    else:
      print("You won and the opponent lost because you chased down the target successfully!")
else:
  print("You lost the toss")
  tossopt = random.choice(tossvar)
  if (tossopt == 1):
    print("Computer has chosen to bowl!")
    print("Its your turn to bat!!")
    while (runs!=rand):
      runs = int(input('Enter the run '))
      if (0<runs<=6):
        rand = random.choice(num)
        print(rand)
        if (runs == rand):
          print("Out!!")
          print("Its your turn to bowl now!")
          print("Your final score is",score)
          print("Opponent needs",score+1,"runs to win!")
        else:
          score = score + runs
          print("Your current score is",score)
      else:
        print("Enter run less than or equal to 6")
    total=0
    while (total<=score):
      runs=int(input('Enter the run '))
      if (0<runs<=6):
        rand = random.choice(num)
        print(rand)
        if (runs == rand):
          print("Out!!")
          print("You won and opponent lost by",(score-total),"runs!")
          print("Opponent's final score is",total)
          exit()
        else:
          total = total + rand
          print("Opponenet's current score is",total)
      else: 
        print("Enter run less than or equal to 6")
    else:
      print("You lost and the opponent won because the opponent chased down the target successfully!")
  if (tossopt == 2):
    print("Computer has chosen to bat!")
    print("Its your turn to bowl!!")
    score = 0
    while (runs!=rand):
      runs = int(input('Enter the run '))
      if (0<runs<=6):
        rand = random.choice(num)
        print(rand)
        if (runs == rand):
          print("Out!!")
          print("Its your turn to bat now")
          print("Opponent's final score is",score)
          print("You need",score+1,"runs to win!")
        else:
          score = score + rand
          print("Opponent's current score is",score)
      else: 
        print("Enter run less than or equal to 6")
    total=0
    while (total<=score):
      runs = int(input('Enter the run '))
      if (0<runs<=6):
        rand = random.choice(num)
        print(rand)
        if (runs == rand):
          print("Out!!")
          print("You lost and opponent won by",(score-total),"runs!")
          print("Your final score is",total)
          exit()
        else:
          total = total + runs
          print("Your current score is",total)
      else:
        print("Enter run less than or equal to 6")
    else:
      print("You won and the opponent lost because you chased down the target successfully!")