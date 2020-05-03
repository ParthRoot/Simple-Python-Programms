num=int(input("Enter the number:"))
n1=0
n2=1
count=0
if num <= 0:
    print("enter the positive number")
else:
    print("fibonacci sequnce")
    while count < num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1

