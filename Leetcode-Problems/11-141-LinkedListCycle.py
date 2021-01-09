## Reverse a singly linked list.

# In this we are going to solve leetcode problem #206
# https://leetcode.com/problems/reverse-linked-list/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- given a head node of a singly linked list
  # Output -- true if cycle is present, else False
  # Egde Cases -- only head node in linked list, 
  # Assumptions -- just keep in mind these constraints
        Constraints:
          The number of the nodes in the list is in the range [0, 104].
          -105 <= Node.val <= 105
          pos is -1 or a valid index in the linked-list.





# Actual code --
## Solution 1: 

''' 
Pseudo code  --
      - while we haven't hit the tail
        - does "Set" has node, if yes we have cycle
        - otherwise add node to set
        - out of list, return false
'''

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        on = head
        while on:
            if on in s:
                return True
            s.add(on)
            on = on.next
        return False

## Big-O notation -->
# time complexity --> O(n) --> because of while loop
## space complexity --> O(n) --> because of set


## Solution 2:-
''' 
Pseudo code  --
      - while we haven't hit the tail
        -- advance fast by 2 nodes
        -- advance slow by one node
        -- if fast == slow, we have a cycle
        -- else return false
'''

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast:
            if fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
'''
## Big-O notation -->
# time complexity --> O(n) --> but keep few things in mind
      -- if we have a cycle, time complexity would be O(n) + O(k), because fast node iterating to cycle more than n nodes, but overall it will be O(n)
      -- if we don't have a cycle, time complexity would be O(n/2) because fast node will end of list sooner, but overall it will be O(n)
      -- its good to discribe this in interview, so that interviewer know that you have some background knowledge
## space complexity --> O(1) --> as we not using any extra space other than few variables
'''

## Solution 3:-- another faster approach
def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

'''
## Big-O notation -->
# time complexity --> O(n) --> but overall time distribution is lesser than as we are using exception handling method
## space complexity --> O(1) --> as we are not using any extra space other than few variables
'''
