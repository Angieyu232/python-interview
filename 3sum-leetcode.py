'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Remove duplicate answers

time complexity n**2

'''


class Solution:



    def twoSumII(self, nums: List[int], index: int, res: List[List[int]]):
        lo, hi = index + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[index] + nums[lo] + nums[hi]
            if sum < 0 or (lo > index + 1 and nums[lo] == nums[lo - 1]):
                # when there are duplicates, needed to be included in this lo += 1
                lo += 1
            elif sum > 0 or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                # when there are duplicates in the right side
                hi -= 1
            else:
                #when sum == 0
                res.append([nums[index], nums[lo], nums[hi]])
                lo += 1
                hi -= 1


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            # remove duplicates
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res


