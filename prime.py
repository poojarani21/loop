i=2
num=int(input("enter any number"))
while i<num:
    if num%i==0:
        print(num,"is not a prime number")
        break
    i=i+1
else:
    print(num,"num is a prime number")