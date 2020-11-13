n=int(input())
a=list(map(int,input().split()))
i=1
while i<n and a[i-1]<a[i]:
	i+=1
j=i
while j<n and a[j-1]>a[j]:
	j+=1
x=a[:i-1]+a[i-1:j][::-1]+a[j:]
s=sorted(a)
if x==s :
	print("yes")
	print(i,j)
else:
	print("no")