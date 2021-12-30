n=int(input("enter any number"))
i=0
sum=0
while n!=0:
	r=n%10
	sum=sum+r*pow(2,i)
	n=n//10
	i+=1
print(sum)