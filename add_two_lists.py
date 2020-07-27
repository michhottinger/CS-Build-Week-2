This can hold the two linked list problem
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode()
        head = result
        carry = 0

        
        while l1 or l2: 

            if l1: 
                num_1 = l1.val
                l1 = l1.next
            else: 
                num_1 = 0
                
            if l2:
                num_2 = l2.val
                l2 = l2.next
            else: 
                num_2 = 0
            
            sum_num = num_1 + num_2 + carry
            
            if sum_num > 9 : 
                result.next = ListNode(sum_num%10)
                carry = 1
                
            else: 
                result.next = ListNode(sum_num)
                carry = 0
            result = result.next
            
            if carry == 1:
                result.next = ListNode(carry)
            
        return head.next
