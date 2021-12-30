num=int(input("enter any number"))
product=1
while num>0:
    product=product*num%10
    num=num//10
print(product)