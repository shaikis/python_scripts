n=20
i = 1
for i in range(n):
    if i % 5 == 0 and i % 3 == 0:
        print("FizBuzz")
    elif i % 2 == 0 : 
        print("Fiz")
    else :
        print(i)      
        