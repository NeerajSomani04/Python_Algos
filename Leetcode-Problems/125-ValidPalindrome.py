# In this we are going to solve leetcode #387 problem
# https://leetcode.com/problems/valid-palindrome/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- any printable ASCII characters in the form of string
  # Output -- "true" if valid palindrome, else "false"
  # Egde Cases -- empty string is a valid palindrome, also string might contain special charchater
  # Assumptions -- remove special charachters, also, upper case and lower case letters are same

## Pointer menthod or Pointer Traversal is a great way to solve this problem


''' Pseudo code  --
      compare original string with reverse of it 
'''
# What is Naive solution:-
   # Its a solution that seems very obvious but usually not very efficient
   # Sometime interviewer wants to check, candidates know naive solution or not. Or build from Naive solution to best solution.
   # A big part of solving problem is comparing different solutions
  
    
    
# Actual code --
## Solution 1:

def isPalindrome(s):
  return ''.join(reversed(s)) == s

## Big-O 
# time complexity --> O(n) + O(n) ==> O(2n) ==> O(n)
    # join and reverse function both uses O(n) time
# space complexity --> O(n)
    # join and reverse function going to use temporary space to store string value.

## Note: Above solution wouldn't work completely because we have special charachter in the input values.

## why we can't use Hash table in it:-
    # if we create hash table, we need extra space to store values in it, apart from processing space needed
    # hash table also doesn't guarantee order of charachters. which is essential in this problem.

# Solution 2:
def isPalindrome(s):
  clean_string = ''.join(filter(str.isalnum, s)).lower()
  return ''.join(reverse(clean_string)) == clean_string

# time complexity --> O(n) (each O(n) for each funtion like join, filter, lower)
# space complexity --> O(n) (each function need some temp space for storage and for clean_string variable)

## can we do anything better to solve this:
# we can use pointer traversal

# Solution 3:

''' Pseudo code --
      - create left and write pointers (represented by indices)
      - while pointers haven't meet
          - check if charachters are same
          - move pointers towards center
'''

# Actual code:
def isPalindrome(s):
  clean_string = ''.join(filter(str.isalnum, s)).lower()
  i = 0
  j = length(clean_string)-1
  
  while(i < j) :
    if clean_string[i] == clean_string[j]:
      i += 1
      j -= 1
    else: 
      return False
  return True

# time complexity --> O(n) (each O(n) for each funtion like join, filter, lower)
      # here, while loop is only running for O(n/2) but that is considered as O(n) only
# space complexity --> O(n) (each function need some temp space for storage and for clean_string variable)


# Question for Aaron:- 
  # you mentioned in solution 3, space complexity is O(1) but in reality you are not considering the space used for cleaning the string and hence, space complexity of the solution itself in O(n).
  
