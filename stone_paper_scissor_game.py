"""
1- Input from user :(Rock, Paper, Scissor)
2-computer choice(use module random)
3-print result

Cases:
Case A
Rock=Rock :Tie
Rock=Paper :Paper win
Rock=Scissor :Rock win

Case B
Paper=Paper :Tie
Paper=Rock :Paper win
Paper=Scissor :Scissor win

Case C
Scissor=Scissor :Tie
Scissor=Rock :Rock win
Scissor=Paper :Scissor win   """
import random
random_choice = ["Rock","Paper","Scissor"]
user_choice=input("inter your move =Rock , Paper, Scissor :")
comp_choice=random.choice(random_choice)
print(f"User Choice ={user_choice}, Computer Choice ={comp_choice}")

if user_choice==comp_choice:
    print("Both chooses same : Match Tie")
elif user_choice=="Rock":
    if comp_choice =="Paper":
        print("Paper covers Rock = Computer Win ...")
    else:
        print("Rock smashed Scissor = You Win ...")
elif user_choice =="Paper":
    if comp_choice =="Scissor":
        print("Scissor cuts Paper = Computer win...")
    else:
        print("Paper covers Rock = You win...")
elif user_choice =="Scissor":
    if comp_choice =="Paper":
        print("Scissor cuts paper = You Win...")
    else:
        print("Rock samshed Scissor = computer Win...")
