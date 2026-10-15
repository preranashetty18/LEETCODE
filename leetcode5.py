#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import Optional, List

# 1. Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 2. Main Solution Class
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            # Reverse group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            
        return dummy.next

    def getKthNode(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

# 3. Utility Functions for Jupyter Verification
def build_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# --- EXECUTING TEST CASES IN JUPYTER ---
sol = Solution()

# Example 1
arr1 = [1, 2, 3, 4, 5]
k1 = 2
head1 = build_linked_list(arr1)
output_head1 = sol.reverseKGroup(head1, k1)
print("--- Example 1 ---")
print(f"Input:  head = {arr1}, k = {k1}")
print(f"Output: {linked_list_to_list(output_head1)}\n")

# Example 2
arr2 = [1, 2, 3, 4, 5]
k2 = 3
head2 = build_linked_list(arr2)
output_head2 = sol.reverseKGroup(head2, k2)
print("--- Example 2 ---")
print(f"Input:  head = {arr2}, k = {k2}")
print(f"Output: {linked_list_to_list(output_head2)}")


# In[ ]:




