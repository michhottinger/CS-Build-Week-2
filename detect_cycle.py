#detect if linked list is in a cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = head #start at head of list
        dict = {}#create a cool dict for adding nodes
        while(cur):
            if(cur in dict):
                return cur#return the value if its in the dict already
            else:
                dict[cur] = True#otherwise keep going forward
            cur = cur.next
        return None
