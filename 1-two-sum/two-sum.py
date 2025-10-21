class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n1, number1 in enumerate(nums) :
            for n2, number2 in enumerate(nums):
                if ((number1 + number2) == target) and (n1 != n2):
                    return [n1,n2]


        