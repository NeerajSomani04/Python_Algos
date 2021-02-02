# In this we are going to solve leetcode #3 problem
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

''' Pattern : this question can be solved using following pattern
## all these technique solutions available on leetcode

# sliding window pattern
# two pointer technique
# four pointer technique
'''

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input --
  # Output --
  # Egde Cases --
  # Assumptions --

''' Pseudo code  --

'''

# Actual code --
# Solution 1:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        windowStart = 0
        windowElements = {}
        maxWindowLength = float('-inf')

        for i, v in enumerate(s):
            if v not in windowElements:
                windowElements[v] = 1
            else:
                windowElements[v] += 1

            while max(windowElements.values())>1:
                windowElements[s[windowStart]] -= 1
                if windowElements[s[windowStart]] == 0:
                    del windowElements[s[windowStart]]
                windowStart += 1

            maxWindowLength = max(maxWindowLength, len(windowElements))

        return maxWindowLength


''' Big-O efficiency
time complexity - O(n) - because of for loop for entire array
space complexity - O(k) - unique substring character
memory - 14.4 MB
Runtime - 176 ms (20 % faster only)
'''

# Solution 2:

def lengthOfLongestSubstring(self, s: 'str') -> 'int':
    maxlen = 0
    currentlen = 0
    indHash = {}
    leftside = -1
    ls = len(s)
    for ind, ch in enumerate(s):
        if (ch in indHash) and (leftside < indHash[ch]):
            leftside = indHash[ch];
        currentlen = ind - leftside;
        if currentlen > maxlen:
            maxlen = currentlen
        indHash[ch] = ind
    currentlen = ls - leftside - 1
    if currentlen > maxlen:
        maxlen = currentlen
    return maxlen

''' Big-O efficiency
time complexity - O(n) - because of for loop for entire array
space complexity - O(k) - unique substring character
memory - 14.4 MB
Runtime - 72 ms (51 % faster only)
'''

# solution 3:

class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength

''' Big-O efficiency
time complexity - O(n) - because of for loop for entire array
space complexity - O(k) - unique substring character
memory - 14.4 MB
Runtime - 48 ms (96 % faster only)
'''
