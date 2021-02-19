import random
rps=['Stone','Paper','Scissors']
print("Let's Play Rock-Paper-Scissors!")
positive=['1', 'y', 'Y', 'yes', 'Yes', 'YES']
rules="1. Rock breaks scissors\n2. Scissors cut paper\n3. Paper covers rock"
rul=str(input("Would you like to know the rules? "))
if rul in positive:
    print(rules)
else:
    print("Cool!")
print("Alright! Let's play Stone-Paper-Scissor!")
def chances():
    comp_score=0
    user_score=0
    while comp_score<5 and user_score<5:
        user_choice=str(input("Make your choice (Stone/Paper/Scissors)\n> "))
        comp_choice=random.choice(rps)
        if user_choice.title() in rps:
            print("Computer Chose:",comp_choice)
            if user_choice.title()==comp_choice:
                print("Both are same! No points!")
            elif user_choice.title()=="Stone":
                if comp_choice=="Paper":
                    print("Computer took the point!")
                    comp_score+=1
                elif comp_choice=="Scissors":
                    print("You have taken the point!")
                    user_score+=1
            elif user_choice.title()=="Paper":
                if comp_choice=="Stone":
                    print("You have taken the point!")
                    user_score+=1
                elif comp_choice=="Scissors":
                    print("Computer took the point!")
                    comp_score+=1
            elif user_choice.title()=="Scissors":
                if comp_choice=="Stone":
                    print("Computer took the point!")
                    comp_score+=1
                elif comp_choice=="Paper":
                    print("You have taken the point!")
                    user_score+=1
        else:
            print("Invalid Input.")
            break
        print("Current Standings:\nYour Score = {}\nComputer Score = {}".format(user_score,comp_score))
    refree(user_score,comp_score)
def refree(user_score,comp_score):
    if user_score==5:
        print("You Win!")
    elif comp_score==5:
        print("Computer Wins!")
    comp_score=0
    user_score=0
    ans=str(input("Would you like to play again? "))
    if ans in positive:
        chances()
chances()