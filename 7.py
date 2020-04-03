n=int(input())
nums=list(map(int, input().split()))
num=[]
high=nums[0]
num.append(high)
for i in range(0,n):
    if i+1>=n:
        break
    elif high<nums[i+1]:
        high=nums[i+1]
        num.append(high)
for n in num:
    print(n,end=' ')