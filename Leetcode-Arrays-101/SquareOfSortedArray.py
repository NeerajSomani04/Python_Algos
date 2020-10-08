## Solution that I came up with:-

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        for _ in A:
            result.append(_*_)
        return sorted(result)


''' Big-O efficiency :-
- time complexity - O(n log n) - because of for loop and sorted function
- space complexity - O(n) - need to store square of every number
'''

# Solution from Discussion -
# Alternate Solution :- Approach : Two Pointer
## one possible way:
class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans


## Best possible solution i found so far:-
def sortedSquares(self, A: List[int]) -> List[int]:

    B = [val**2 for val in A]

    l, r = 0, len(B) - 1
    results = []

    while l <= r:
        if B[l] > B[r]:
            results.append(B[l])
            l += 1
        else:
            results.append(B[r])
            r -= 1

    return results[::-1]

'''
Big-O efficiency -
time complexity - O(n) because of for and while loop
space complexity - O(n) because of array B and results
'''
