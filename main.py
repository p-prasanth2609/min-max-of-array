a=list(map(int,input().split()))
max=a[0]
min=a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
    if min>a[i]:
        min=a[i]
print(min+max)




