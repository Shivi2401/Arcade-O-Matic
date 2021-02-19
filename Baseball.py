import random
toss=["Heads","Tails"]
types=["Strike","Defend"]
plays=[1,2,3,4,5,6]
rules="1. On the basis of a toss, it'll be decided who strikes first.\n2. When prompted, the user inputs their number (1-6).\n3. If the numbers chosen by the striker and pitcher are the same, it counts as a home run.\n4. If they are different, it counts as a strike.\n5. Once 3 strikes are reached, the striker's turn is finished.\n6. The higher score, after both have played 5 turns, wins."
positive=['1','y','Y','yes','Yes','YES']
a=str(input("Would you like to see the rules? "))
if a in positive:
    print(rules)
else:
    print("Cool!")
print ("Let's play baseball!")
while True:
    b=str(input("Toss! Player, what will you choose?"))
    c=random.choice(toss)
    if b.title()==c and b.title() in toss:
        d=str(input("You won the toss! Would you like to strike or defend?"))
        if d.title() in types:
            if d.title()=='Strike':
                print("Begin!")
                strikes=0
                runs_user=0
                turner=0
                while turner<5 and strikes<3:
                    us_num=int(input("Pick your number!"))
                    co_num=random.choice(plays)
                    print("The computer has chosen",co_num)
                    if us_num==co_num:
                        runs_user+=1
                        print("You scored a run!")
                    else:
                        strikes+=1
                    turner+=1
                print("Good run, your final score is:",runs_user)
                strikes=0
                print("Computer's turn.")
                print("Begin!")
                strikes=0
                runs_co=0
                turner=0
                while turner<5 and strikes<3:
                    us_num=int(input("Pick your number!"))
                    co_num=random.choice(plays)
                    print("The computer has chosen",co_num)
                    if us_num==co_num:
                        runs_co+=1
                        print("Computer scored a run!")
                    else:
                        strikes+=1
                    turner+=1
                print("The computer's final score is:",runs_co)
            elif d.title()=='Defend':
                print("Begin!")
                strikes=0
                runs_co=0
                turner=0
                while turner<5 and strikes<3:
                    us_num=int(input("Pick your number!"))
                    co_num=random.choice(plays)
                    print("The computer has chosen",co_num)
                    if us_num==co_num:
                        runs_co+=1
                        print("Computer scored a run!")
                    else:
                        strikes+=1
                    turner+=1
                print("The computer's final score is:",runs_co)
                strikes=0
                print("Your Turn!")
                print("Begin!")
                strikes=0
                runs_user=0
                turner=0
                while turner<5 and strikes<3:
                    us_num=int(input("Pick your number!"))
                    co_num=random.choice(plays)
                    print("The computer has chosen",co_num)
                    if us_num==co_num:
                        runs_user+=1
                        print("You scored a run!")
                    else:
                        strikes+=1
                    turner+=1
                print("Good run, your final score is:",runs_user)
            else:
                print("")
    elif b.title()!=c and b.title() in toss:
        print("The computer won the toss.")
        d=random.choice(types)
        print("The computer has chosen:",d)
        if d=="Strike":
            print("Begin!")
            strikes=0
            runs_co=0
            turner=0
            while turner<5 and strikes<3:
                us_num=int(input("Pick your number!"))
                co_num=random.choice(plays)
                print("The computer has chosen",co_num)
                if us_num==co_num:
                    runs_co+=1
                    print("Computer scored a run!")
                else:
                    strikes+=1
                turner+=1
            print("The computer's final score is:",runs_co)
            strikes=0
            print("Your Turn!")
            print("Begin!")
            strikes=0
            runs_user=0
            turner=0
            while turner<5 and strikes<3:
                us_num=int(input("Pick your number!"))
                co_num=random.choice(plays)
                print("The computer has chosen",co_num)
                if us_num==co_num:
                    runs_user+=1
                    print("You scored a run!")
                else:
                    strikes+=1
                turner+=1
            print("Good run, your final score is:",runs_user)
        else:
            print("Begin!")
            strikes=0
            runs_user=0
            turner=0
            while turner<5 and strikes<3:
                us_num=int(input("Pick your number!"))
                co_num=random.choice(plays)
                print("The computer has chosen",co_num)
                if us_num==co_num:
                    runs_user+=1
                    print("You scored a run!")
                else:
                    strikes+=1
                turner+=1
            print("Good run, your final score is:",runs_user)
            strikes=0
            print("Computer's turn.")
            print("Begin!")
            strikes=0
            runs_co=0
            turner=0
            while turner<5 and strikes<3:
                us_num=int(input("Pick your number!"))
                co_num=random.choice(plays)
                print("The computer has chosen",co_num)
                if us_num==co_num:
                    runs_co+=1
                    print("Computer scored a run!")
                else:
                    strikes+=1
                turner+=1
            print("The computer's final score is:",runs_co)
    elif b.title()!=c and b.title() not in toss:
        print("Invalid input, please toss again!")
        runs_user,runs_co=-1,-1
    if runs_user>runs_co and runs_user!=-1 and runs_co!=-1:
        print("You won!")
    elif runs_user==runs_co and runs_user!=-1 and runs_co!=-1:
        print("It's a draw!")
    elif runs_user!=-1 and runs_co!=-1:
        print("You lost.")