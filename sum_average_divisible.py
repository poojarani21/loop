i=1
average=0
sum=0
while i<=11:
    num=int(input("enter any number"))
    sum=sum+num
    # print(sum)
    i=i+1
    average=sum/11
print(sum)
print(average)
if average%5==0:
    print("divisible")
else:
    print("not divisible")
