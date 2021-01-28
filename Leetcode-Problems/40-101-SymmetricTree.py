# In this we are going to solve leetcode #101 problem
# https://leetcode.com/problems/symmetric-tree/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- any string character is allowed
  # Output -- single integer (that represent index value of first unique character and "-1" if no unique character)
  # Edge Cases -- An array can be empty or An array can have no unique character
  # Assumptions -- An array can contain only alphabets in lowercase, and no numerical or special character

''' Pseudo code  --
'''

# Actual code --
# Solution 1: Iteratively
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        queue = [root, root]
        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if t1 == None and t2 == None:
                continue
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True

''' Big-O efficiency
time complexity - O(n) - because traveling each node of tree once
space complexity - O(n) - There is additional space required for the search queue. In the worst case, we have to insert O(n)O(n) nodes in the queue.
runtime - 24ms
memory - 14.5 MB
'''
## Notes --> above solution adding nodes twice, which is making calculation repetitive

# Solution 2: iteratively (optimised version of solution 1)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
	    # if root is None, return True
        if not root:
            return True
        # create a lst to keep track of **pair of nodes** to check
        pair_to_visit = [(root.left, root.right)]

		# loop on pair_to_visit list
        while pair_to_visit:
		    #
            pair = pair_to_visit.pop()
            left = pair[0]
            right = pair[1]

			# try to return False by checking if the two nodes are not equal
            if left and not right:
                return False
            if not left and right:
                return False
            if left and right:
                if left.val != right.val:
                    return False
				# if two nodes are equal, check if symterric nodes are equal
                pair_to_visit.append((left.right, right.left))
                pair_to_visit.append((left.left, right.right))
		# if there was no False returned above, it must be the case that all the compared nodes are equal
        # and since we compared symmytric nodes to each other, establishing symterical tree
        return True

''' Big-O efficiency
time complexity - O(n) - because traveling each node of tree once
space complexity - O(n) - There is additional space required for the search queue. In the worst case, we have to insert O(n)O(n) nodes in the queue.
runtime - 300 ms --> extra time caused by nested array, that requires few additional steps in calculation
memory - 14.7 MB
'''

# Solution 3: Recursively
