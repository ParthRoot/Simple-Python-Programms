num=int(input("enter the num"))
factorial=1
if num < 0:
    print("sorry factorial doesnot exit negative num")
elif num == 0:
    print("factorial always start 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("the factorial of",num,factorial)