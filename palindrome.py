num=int(input("enter any number"))
temp=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
if temp==rev:
    print(" it is a palindrome number")
else:
    print("it is not a palindrome number")