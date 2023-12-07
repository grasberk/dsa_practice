
# S: given a list of numbers return a list with the numbers in reverse order from the original
# E:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
# Input: head = []
# Output: []
# input: head=[-3,-2,-1,0,1,2,3]
# output=[3,2,1,0,-1,-2,-3]
# A:
# T:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        