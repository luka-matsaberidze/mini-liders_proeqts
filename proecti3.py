import random


motamase_1 = str(input("rock , paper , scissors:  "))


motamase_2 = random.randint(1,3)

if motamase_2 == 1:
    motamase_2 ="rock"
elif motamase_2 ==2:
    motamase_2 = "paper"
elif motamase_2 ==3:
    motamase_2 = "scissors"

print("bot: "+ motamase_2)


if motamase_1 == motamase_2:
    print("its tie!")
elif (motamase_1 == "paper" and motamase_2 == "rock") or(motamase_1=="scissors"and motamase_2 == "paper") or (motamase_1=="rock"and motamase_2=="scissors"):
    print("you win!")
else:
    print("you lose")
  
