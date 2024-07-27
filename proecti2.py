import random

#proeqti agze dakavsirebit

a = int(input("what is your age: "))

b = random.randint(1,10)
print(a+b)

if a+b>=50:
    print("you getting old :D")
elif a+b>=18:
    print("you are adoult")
elif a+b<18 and a+b>=8: 
    print("you are school student")
elif a+b<8 and a+b>3:
    print("you are in the frog")
else:
    print("you are baby")



d


