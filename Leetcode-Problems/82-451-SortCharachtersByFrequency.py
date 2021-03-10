# 451 - 

# Solution 1:

from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        ht = Counter(s)
        print(ht)
        maxHeap = []
        for key, value in ht.items():
            heapq.heappush(maxHeap, (-value, key))

        result = []
        while len(maxHeap) > 0:
            frequency, string = heapq.heappop(maxHeap)
            for i in range(-frequency):
                result.append(string)
        return ("".join(result))
        
'''
Time complexity #
The time complexity of the above algorithm is O(D*logD)O(D∗logD) where ‘D’ is the number of distinct characters in the input string. This means, in the worst case, when all characters are unique the time complexity of the algorithm will be O(N*logN)O(N∗logN) where ‘N’ is the total number of characters in the string.

Space complexity #
The space complexity will be O(N)O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.
'''
