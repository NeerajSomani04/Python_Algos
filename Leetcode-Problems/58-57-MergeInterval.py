## 57 - https://leetcode.com/problems/insert-interval/

## Solution 1: not working

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        intervals.append(new_interval)
        intervals.sort(key=lambda x: x[0])
        if len(intervals) < 2:
            return intervals
        merged = []
        # TODO: Write your code here
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[1] <= end:
                end = max(interval[1], end)
            else:
                merged.append([start,end])
                start = interval[0]
                end = interval[1]
        merged.append([start,end])
        return merged
