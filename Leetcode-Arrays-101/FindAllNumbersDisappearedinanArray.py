# Lets follow our procedure to solve this question:
'''
Definition - can be understood from question (https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/)
Data - 
  - Input - a array that contains some intergers
  - output - return third maximum number in array
  - Edge case - number can vary from any negative to position number, array length can be one to infinity.
  - assumptions - array can't be empty
  
Pseudo code - 
  - create an empty array that contains only 3 maximum element at any iteration of nums array
  - run through each element of array and check if new element is greater than min(array) 
    - replace it
    - return third max of array after sorting it
'''

# Actual Code 

'''
# Solution 1 -
Not able to solve it by myself. After understanding other Solutions from Discussion, I realized a very critical point of this question:-
  -- any element inside the array can't be greater than the size of array, meaning:
  -- this example is not valid array for this question :- [1, 2, 7], because 'n'=3, (n = size of array), and 7 can't be a part of this array for this question.
  -- Now, I can think about the solution provided in discussion
  '''
