import random
x = 150
pc = random.randint(0,100)
y = 0

while pc!=x:
    x = int(input("Δώσε αριθμό από το 0 εώς το 100"))
    if pc > x:
        print("Higher")
        y=y+1

    elif pc<x:
        print("Lower")
        y = y + 1

    else:
        print("Correct")
        y = y + 1

if y>=10 :
    print("Try again", y)

elif y>= 5:
    print("Ok", y )

else:
    print("Good Job", y)










