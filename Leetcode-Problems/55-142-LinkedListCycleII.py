# 142 - https://leetcode.com/problems/linked-list-cycle-ii/


# Solution 1: little bigger interms of verbose (solution2 is smaller version of same)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def calculate_length_cycle(self, slow, head):
        counter = 0
        temp = head
        while slow != temp:
            counter += 1
            temp = temp.next
        return counter
            
    def find_start(self, head, counter):
        pointer1 = head
        pointer2 = head
        for i in range(counter):
            pointer2 = pointer2.next
        
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
            
        
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next # this is same as slow.next because we already incremented slow by 1 position
            if slow == fast:
                position = self.calculate_length_cycle(slow, head)
                break
        if fast is not None and fast.next is not None:
            return self.find_start(head, position)
        else:
            return None
            
# Solution 2:
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                start = head
                while (start != slow):
                    start = start.next
                    slow = slow.next
                return slow
        
        return None


'''
Time Complexity #
As we know, finding the cycle in a LinkedList with ‘N’ nodes and also finding the length of the cycle requires O(N)O(N). Also, as we saw in the above algorithm, we will need O(N)O(N) to find the start of the cycle. Therefore, the overall time complexity of our algorithm will be O(N)O(N).

Space Complexity #
The algorithm runs in constant space O(1)O(1).
'''
