# 973 -- https://leetcode.com/problems/k-closest-points-to-origin/

# Solution 1: from grokking
#answer
from __future__ import print_function
from heapq import *


class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  # used for max-heap
  def __lt__(self, other):
    return self.distance_from_origin() > other.distance_from_origin()

  def distance_from_origin(self):
    # ignoring sqrt to calculate the distance
    return (self.x * self.x) + (self.y * self.y)

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
  maxHeap = []
  # put first 'k' points in the max heap
  for i in range(k):
    heappush(maxHeap, points[i])

  # go through the remaining points of the input array, if a point is closer to the origin than the top point
  # of the max-heap, remove the top point from heap and add the point from the input array
  for i in range(k, len(points)):
    if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
      heappop(maxHeap)
      heappush(maxHeap, points[i])

  # the heap has 'k' points closest to the origin, return them in a list
  return list(maxHeap)


def main():

  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()



'''
Time complexity 
The time complexity of this algorithm is (N*logK) as we iterating all points and pushing them into the heap.
Space complexity 
The space complexity will be O(K) because we need to store ‘K’ point in the heap.
'''

# Solution 2:
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance = []
        for i in points:
            heapq.heappush(distance,(i[0]**2+i[1]**2, i ))
        
        '''    
        above we are cretaing tuple like this
        this is distance array -  [(8, [-2, 2]), (10, [1, 3])]
        '''
        
        print('this is distance array - ', distance)
        
        K_points = []
        for i in range(k):
            K_points.append(heapq.heappop(distance)[1])
        
        '''
        above we are poping all k minimum elements from minHeap (distance)
        and then appending them in k_point array
        this is k-point array -  [[-2, 2]]
        '''
        print('this is k-point array - ', K_points)
        
        return K_points
    
    
        '''
        time complexity - O(n log n)
        space - O(n)
        '''
      
