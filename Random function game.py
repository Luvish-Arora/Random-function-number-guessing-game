import random as r
a=r.randint(0,100)
b=input("Enter your name:- ")
print("\n------------------------------HI",b,"\nWelcome to the game\n------------------------------You have 7 chances to guess the number\n------------------------------")
d=input("Are you ready?\n")
e=0
while d=="YES" or d=="Yes" or d=="yes" or d=="Y" or d=="y":
    for i in range(7):
        c=0
        c=int(input("------------------------------\nEnter number:- "))
        if a==c:
            print("You guessed it right!!\nThank you for playing!!")
            e+=1
            break
        elif a>c:
            print("Think a number bigger than",c,"\nChances left",9-i)
        elif a<c:
            print("Think a number smaller than",c,"\nChances left",9-i)
    if e==0:
        print("------------------------------\nOHH Chance got over\n------------------------------")
        d=input("Do you want play again?\n")
    elif e==1:
        d=input("Do you want play again?\n")



