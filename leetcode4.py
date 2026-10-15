#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        
        # Sort the array to easily handle duplicates and use the two-pointer strategy
        nums.sort()
        
        for i in range(n - 3):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Early termination optimizations to speed up execution
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break # The smallest possible sum is already greater than target
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue # The largest possible sum with this nums[i] is too small

            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # More early termination optimizations
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                
                # Two-pointer approach for the remaining two elements
                left = j + 1
                right = n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum < target:
                        left += 1  # Sum too small, move left pointer right
                    elif current_sum > target:
                        right -= 1 # Sum too large, move right pointer left
                    else:
                        # Found a valid quadruplet
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicate values for the third element
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicate values for the fourth element
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        # Move both pointers past unique elements
                        left += 1
                        right -= 1
                        
        return res

# --- EXECUTING ALL TEST CASES IN JUPYTER ---
sol = Solution()

# Example 1
nums1 = [1, 0, -1, 0, -2, 2]
target1 = 0
print("--- Example 1 ---")
print(f"Input:  nums = {nums1}, target = {target1}")
print(f"Output: {sol.fourSum(nums1, target1)}\n")

# Example 2
nums2 = [2, 2, 2, 2, 2]
target2 = 8
print("--- Example 2 ---")
print(f"Input:  nums = {nums2}, target = {target2}")
print(f"Output: {sol.fourSum(nums2, target2)}")


# In[ ]:




