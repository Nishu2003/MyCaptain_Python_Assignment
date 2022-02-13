print("============= PROGRAM FOR CALCULATING FIBONACII SERIES======================")
print("Enter the number of terms : " ,end=" ")
n=int(input())
n1,n2=0,1
count=0
print("==================================================================================")
if n<=0:
    print("Enter a positive value.... !")
elif n==1:
        print("Fibonacii Series :")
        print(n1)
else:
    print("FIBONACII SERIES :")
    while count<n:
        print(n1,end="  ")
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
