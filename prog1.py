list=[]
n=int(input("enter the elements="))
for i in range(0,n):
    ele=int(input())
    list.append(ele)

print(list)
for i in list:
    nlist=[]
    if(i%2==0):
        nlist.append(i)
        print(nlist)
      
