c=0
for x,y in sorted((list(map(int,input().split()))for _ in range(int(input())))):c=x if y<c else y
print(c)