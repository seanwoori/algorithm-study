N=int(input())
lst=list(map(int, input().split()))

lst.sort()
sm=0
for i in range(1,len(lst)+1):
    sm+=sum(lst[:i])
print(sm)