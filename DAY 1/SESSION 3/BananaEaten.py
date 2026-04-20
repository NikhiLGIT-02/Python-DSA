#Co-Co Eating Banana
pile=[3,6,7,11]
h=8

left=1
right=max(pile)

answer = right
while left<right:
    mid=left+(right-left)//2
    total_hours =0
    for pi in pile:
        total_hours+=(pi+mid-1)//mid
    if total_hours<=h:
        answer=mid
        right=mid-1
    else:
        left=mid+1
print(answer)
