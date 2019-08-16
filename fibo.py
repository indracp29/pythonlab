def fibo(n):
    if n<=1:
       return n
    else:
        return(fibo(n-1)+fibo(n-2))


n=int(input("enter the elements="))
if n<=0:
    print("value cannot be a -ve")
else:
    print("fibonaci sequence:")
    for i in range(0,n):
        print(fibo(i))
