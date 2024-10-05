import random

b=["rock","paper","sissors"]
sum=0
choice=0
winner="*******Winner********"
lose="******Better luck next time******"
while True:
    a=str(input("enter your choice:"))
    c=random.choice(b)
    if a=="rock" and c=="sissors":
        choice+=1
    elif a=="paper" and c=="rock":
        choice+=1
    elif a=="sissors" and c=="paper":
        choice+=1
    elif a=="rock" and c=="rock":
        choice+=0
    elif a=="paper" and c=="paper":
        choice+=0
    elif a=="sissors" and c=="sissors":
        choice+=0
    else:
        sum+=1
    print("opponent choice:",c)
    print("opponent point:->",sum)
    print("your point:->",choice)
    if(choice==10):
        print(winner)
    break
    if(sum==10):
        print(lose)
    break


