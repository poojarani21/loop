num=int(input("enter any number"))
num2=num
while num2>9:
    sum=0
    while num2!=0:
        rem=num2%10
        sum=sum+rem
        num2=int(num2/10)
    num2=sum
if sum==1:
    print(num,"is a magic number")
else:
    print(num,"is not a magic number")









