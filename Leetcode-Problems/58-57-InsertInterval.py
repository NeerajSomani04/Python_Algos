## 57 - https://leetcode.com/problems/insert-interval/

'''
Input - Sorted list of non-overlaping intervals
Output - list of exclusive intervals
Edge case - empty interval
Assumption -
Constraints - 
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105
'''


## Solution 1: 

class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        intervals.append(new_interval)
        intervals.sort(key=lambda x: x[0])
        #print(intervals)
        if len(intervals) < 2:
            return intervals
        merged = []
        # TODO: Write your code here
        start = intervals[0][0]
        end = intervals[0][1]
        #print([start, end])
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                merged.append([start,end])
                start = interval[0]
                end = interval[1]
        merged.append([start,end])
        return merged

'''
## Above approach is 
time complexity - O(n log n)
space complexity - O(n) 
'''

    
## Solution 2:
class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        merged = []
        i, start, end = 0, 0, 1

        # skip (and add to output) all intervals that come before the 'new_interval'
        while i < len(intervals) and intervals[i][end] < new_interval[start]:
            merged.append(intervals[i])
            i += 1

        # merge all intervals that overlap with 'new_interval'
        while i < len(intervals) and intervals[i][start] <= new_interval[end]:
            new_interval[start] = min(intervals[i][start], new_interval[start])
            new_interval[end] = max(intervals[i][end], new_interval[end])
            i += 1

        # insert the new_interval
        merged.append(new_interval)

        # add all the remaining intervals to the output
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        return merged

'''
Time complexity #
As we are iterating through all the intervals only once, the time complexity of the above algorithm is O(N)O(N), where ‘N’ is the total number of intervals.

Space complexity #
The space complexity of the above algorithm will be O(N)O(N) as we need to return a list containing all the merged intervals.
'''
