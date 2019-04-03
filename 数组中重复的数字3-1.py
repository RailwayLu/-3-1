from scipy.spatial.distance import pdist
import numpy as np

def findDuplicates(nums):
    if len(nums)==0:
        return False
    for i in nums:
        if i<1 or i>len(nums)-1:
            return  False
    for i in range(len(nums)):
        while i!=nums[i]-1:
            if nums[i]==nums[nums[i]-1]:
                break
            else:
                temp = nums[nums[i]-1]
                nums[nums[i]-1]=nums[i]
                nums[i] = temp
                # nums[i],nums[nums[i]-1]=nums[nums[i]-1],nums[i]
                # nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]

    return nums
print(findDuplicates([2,3,5,4,5,8,2,3,2,6,7]))