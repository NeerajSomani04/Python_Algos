# 986 - https://leetcode.com/problems/interval-list-intersections/

# Solution 1:
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        f_len = len(firstList)
        s_len = len(secondList)
        
        if f_len < 1 or s_len < 1:
            return []
        i = 0
        j = 0
        result = []
        while i < f_len and j < s_len:
            
            a_overlaps_b = firstList[i][0] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]
            
            b_overlaps_a = secondList[j][0] >= firstList[i][0] and secondList[j][0] <= firstList[i][1]
            
            if (a_overlaps_b or b_overlaps_a):
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                result.append([start, end])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return result

'''
Time complexity #
As we are iterating through both the lists once, the time complexity of the above algorithm is O(N + M)O(N+M), where ‘N’ and ‘M’ are the total number of intervals in the input arrays respectively.

Space complexity #
Ignoring the space needed for the result list, the algorithm runs in constant space O(1)O(1).

'''
