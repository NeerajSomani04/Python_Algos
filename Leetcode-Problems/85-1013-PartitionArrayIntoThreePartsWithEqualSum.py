# Solution 1:

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0: return False
        count, cumsum, target = 0, 0, total // 3
        for num in arr:
            cumsum += num
            if cumsum == target:
                cumsum = 0
                count += 1
        return count >= 3

'''
A good explaination here:-
Because in example [1, -1, 1, -1, 1, -1, 1, -1] the count will turn out to be 4 but you could still divide this array in three parts... [1,-1] and [1,-1,1,-1] and [1,-1] the sums are same for these three arrays but the count in the code counts more. Hope it helps.
'''
