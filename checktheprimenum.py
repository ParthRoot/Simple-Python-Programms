num = int(input("Enter the number\n"))
if num > 1:
    for i in range(2,num // 2):
        if num % i == 0:
            print("this is not the prime number")
            break
    else:
        print("this is a prime number")

