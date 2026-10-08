#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import Optional

# 1. Define the ListNode class so Python knows what a linked list node is
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper method to print the linked list visually in your notebook
    def __repr__(self):
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return "[" + ",".join(nodes) + "]"

# 2. The LeetCode Solution class
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 if list1 else list2
        return dummy.next

# 3. Helper function to turn normal Python lists into LeetCode Linked Lists
def build_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# =========================================================================
# RUNNING LEETCODE EXAMPLE 1
# Input: list1 =, list2 = [1,3,4]
# Expected Output: [1,1,2,3,4,4]
# =========================================================================

# Create the inputs
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])

print("Input List 1: ", list1)
print("Input List 2: ", list2)

# Run the merge solution
sol = Solution()
merged_head = sol.mergeTwoLists(list1, list2)

# Print the final result
print("Merged Output:", merged_head)


# In[ ]:




