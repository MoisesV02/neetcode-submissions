class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index

        for index, value in enumerate(nums):
            difference = target - value

            #Checks if the difference is in the hashmap, if it is it returns the its 
            #index and the current index
            if difference in prevMap:
                return [prevMap[difference], index]

            #Hashmap is updated to containe the value key and the index of that value
            prevMap[value] = index
        