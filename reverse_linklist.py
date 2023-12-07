
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
# step1 check for if array is empty and if so return the array
# step2 create 3 pointers for previous value, current value and next value
# step3 check the next node value and if there is a value, then we assign curr value as next value and current value as previous value




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        