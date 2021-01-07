# In this we are going to solve leetcode #49 problem
# https://leetcode.com/problems/group-anagrams/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an array of strings (alphabets in lowercase, no numerical or special charachter)
  # Output -- an array of array of strings (return the strings grouped by anagrams)
  # Egde Cases -- An array can have empty string (empty array not allowed as per problem definition)
  # Assumptions -- Considering only complete matches of strings, partial match doesn't count.

''' Pseudo code  --
      loop through array of string
        - sort each string value of array
        - if sorted key already into hash table as key, append original string to array as value
        - if sorted key not exist in hash table as key, then add it as key and add original string to array as value        
'''

# Actual code --
# Solution 1:

def groupAnagrams(strs):
  ht = {}
  for s in strs:
    sorted_string = ''.join(sorted(s))
    ## here sort function returns an array of charachters and hence we need to use join method to combine each char back and get sorted string
    if sorted_string in ht:
      ht[sorted_string].append(s)
    else:
      ht[sorted_string] = [s]
  return ht.values()
 
 '''
  ## Big-O efficiency --
  # time complexity: O(n) * O(m log m)
    -- O(n) - for for loop (n is number of strings provided in a given array)
    -- O(m log m) - for "in-built" sort function (m is max number of charachters in a string)
 
  # space complexity: O(n) --> linear space
    -- O(n) - considering every string is unque in array and hence hash table
 '''   
 
 
 
    
    
    
