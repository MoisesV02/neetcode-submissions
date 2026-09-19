class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value = None
        nums.sort()
        for i in nums:
            if (value == None):
                value = i
                continue
            
            elif (value == i):
                return True

            value = i

        return False

        