from cs50 import get_float

while True:
    n=get_float("Change owed: ")
    if n>0:
        break
amount = n*100
coins=0

while amount>=25:
    amount = amount-25
    coins+=1

while amount>=10:
    amount = amount-10
    coins+=1

while amount>=5:
    amount = amount-5
    coins+=1

while amount>=1:
    amount = amount-1
    coins+=1

print(coins)
