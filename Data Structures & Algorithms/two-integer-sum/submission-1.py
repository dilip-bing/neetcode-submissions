class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        # iterate nums
        for loop in range(0,len(nums)):
            # check if any value is present in dictionary already
            if nums[loop] in dictionary:
                return sorted([loop,dictionary.get(nums[loop],0)])
            else :
                # calculate complement
                # store positions it in dict
                dictionary[target-nums[loop]] = loop
                # dict[8] = 2
                # dict[5] = 1

        return [-1,-1]


# I : array of num
#  O number
# Hashmap style