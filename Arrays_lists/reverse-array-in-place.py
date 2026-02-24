from typing import List

def reverseArray(nums: List[int]) -> List[int]:
    i=0
    j=len(nums)-1
    while i<j:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
    return nums
    pass

# Read input
nums = list(map(int, input().split()))
result = reverseArray(nums)
print(' '.join(map(str, result)))