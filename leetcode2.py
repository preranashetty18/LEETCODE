#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case: If the array is empty, there are 0 unique elements
        if not nums:
            return 0
        
        # 'write_index' tracks where the next unique element should be placed
        write_index = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
                
        # 'write_index' represents the number of unique elements (k)
        return write_index

# --- TEST CASES AND VERIFICATION DRIVER ---
sol = Solution()

# Test Case 1
nums1 = [1, 1, 2]
print("--- Test Case 1 ---")
print(f"Initial array: {nums1}")
k1 = sol.removeDuplicates(nums1)
print(f"Returned k: {k1}")
print(f"Modified array up to index k: {nums1[:k1]}")
print(f"Full array state: {nums1}\n")

# Test Case 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print("--- Test Case 2 ---")
print(f"Initial array: {nums2}")
k2 = sol.removeDuplicates(nums2)
print(f"Returned k: {k2}")
print(f"Modified array up to index k: {nums2[:k2]}")
print(f"Full array state: {nums2}")


# In[ ]:




