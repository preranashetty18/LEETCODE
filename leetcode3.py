#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Sort the array to easily handle duplicates and use the two-pointer strategy
        nums.sort()
        
        for i in range(len(nums) - 2):
            # If the current number is greater than 0, three positive numbers cannot sum to 0
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element of the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Initialize two pointers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Sum is too small, move left pointer right
                elif total > 0:
                    right -= 1 # Sum is too large, move right pointer left
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the second element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the third element
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers past the processed unique elements
                    left += 1
                    right -= 1
                    
        return res

# --- EXECUTING ALL TEST CASES IN JUPYTER ---
sol = Solution()

# Example 1
nums1 = [-1, 0, 1, 2, -1, -4]
print("--- Example 1 ---")
print(f"Input:  {nums1}")
print(f"Output: {sol.threeSum(nums1)}\n")

# Example 2
nums2 = [0, 1, 1]
print("--- Example 2 ---")
print(f"Input:  {nums2}")
print(f"Output: {sol.threeSum(nums2)}\n")

# Example 3
nums3 = [0, 0, 0]
print("--- Example 3 ---")
print(f"Input:  {nums3}")
print(f"Output: {sol.threeSum(nums3)}")


# In[ ]:




