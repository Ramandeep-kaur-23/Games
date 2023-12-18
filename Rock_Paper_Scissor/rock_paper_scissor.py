#Rock paper scissor game
import random
moves=["rock","paper","scissor"]
while True:
    ucount=0
    ccount=0
    uc = int(input('''
Game started....
You will have three rounds...
Do you want to play?
Press 1 if yes.... 
1 Yes
2 No
    '''))
    if uc<=1:
        for a in range(1,4):
            userinput = int(input('''
Enter 1 for Rock, 2 for Paper, 3 for Scissor.....
1 rock
2 paper
3 scissor'''))
            if userinput == 1:
                un = "rock"
            elif userinput == 2:
                un = "paper"
            cn = random.choice(moves)
            if cn == un:
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif(un=="rock" and cn=="scissor") or (un=="paper" and cn=="rock") or (un=="scissor" and cn=="paper"):
                print("computer's choice",cn)
                print("Your choice",un)
                print("You Win")
                ucount=ucount+1
            else:
                print("computer's choice",cn)
                print("Your choice",un)
                print("Computer Win")
                ccount=ccount+1
            if ucount == ccount:
                print("Final game draw")
                print("user value",ucount)
                print("Computer value",ccount)
        else:
            break
                
            
