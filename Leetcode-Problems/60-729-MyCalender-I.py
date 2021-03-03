# 729 - https://leetcode.com/problems/my-calendar-i/

# Solution 1: this solution works but not best 
class MyCalendar:

    def __init__(self):
        self.events = []
        
    def find_intersection(self, start: int, end: int) -> bool:
        if len(self.events) < 1:
            return False
        
        for index, event in enumerate(self.events):
            a_overlap_b = event[0] >= start and event[0] < end
            b_overlap_a = start >= event[0] and start < event[1]
            if a_overlap_b or b_overlap_a:
                return True
        return False
        
    def book(self, start: int, end: int) -> bool:
        intersection = self.find_intersection(start,end)
        if intersection:
            return False
        else:
            self.events.append([start, end])
            return True

'''
Complexity Analysis

Time Complexity: O(N^2), where N is the number of events booked. For each new event, we process every previous event to decide whether the new event can be booked. 
Space Complexity: O(N), the size of the events array.
'''

# Solution 2 - A balanced tree would be a better approach, meaning if we keep all intervals in sorted order we don't need to process every interval every time.

