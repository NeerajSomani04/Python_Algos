class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        for _ in A:
            result.append(_*_)
        return sorted(result)


''' Big-O efficiency :-
- time complexity - O(n) - because of for loop
- space complexity - O(n) - need to store square of every number
'''
