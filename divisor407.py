def divisor(num):
    for i in range(1,num):
        if num%i==0:
           print(i,end="")

num=int(input("enter a number"))
print("divisor of",str(num),"are")
divisor(num) 
