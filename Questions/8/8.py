n,t=map(int,input().split())

l=list(map(int,input().split()))

i,j,s=0,0,0

for j in range(n):

  s+=l[j]

  if s>t:

    s-=l[i]

    i+=1
    
print(n-i)