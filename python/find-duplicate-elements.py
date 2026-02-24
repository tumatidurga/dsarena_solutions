from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    # Your code here
    pass

# Read input
nums = list(map(int, input().split()))
result = findDuplicates(nums)
print(' '.join(map(str, result)) if result else 'None')