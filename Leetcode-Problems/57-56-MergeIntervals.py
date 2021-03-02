## 56 - https://leetcode.com/problems/merge-intervals/

# Solution 1:
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        
        intervals.sort(key = lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]
        mergedInterval = []
        
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                mergedInterval.append([start, end])
                start = interval[0]
                end = interval[1]
        
        mergedInterval.append([start,end])
        return mergedInterval

'''
Time complexity 
The time complexity of the above algorithm is O(N * logN), where ‘N’ is the total number of intervals. 
We are iterating the intervals only once which will take O(N), in the beginning though, 
since we need to sort the intervals, our algorithm will take O(N * logN).
Space complexity 
The space complexity of the above algorithm will be O(N) as we need to return a list containing all the merged intervals. 
We will also need O(N) space for sorting. 
For Java, depending on its version, Collection.sort() either uses Merge sort or Timsort, and both these algorithms need O(N) space. 
Overall, our algorithm has a space complexity of O(N).
'''      
      
## Solution 2: below solution is with more details, but overall same approach

from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals):
  if len(intervals) < 2:
    return intervals

  # sort the intervals on the start time
  intervals.sort(key=lambda x: x.start)

  mergedIntervals = []
  start = intervals[0].start
  end = intervals[0].end
  for i in range(1, len(intervals)):
    interval = intervals[i]
    if interval.start <= end:  # overlapping intervals, adjust the 'end'
      end = max(interval.end, end)
    else:  # non-overlapping interval, add the previous internval and reset
      mergedIntervals.append(Interval(start, end))
      start = interval.start
      end = interval.end

  # add the last interval
  mergedIntervals.append(Interval(start, end))
  return mergedIntervals


def main():
  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
  print()


main()
