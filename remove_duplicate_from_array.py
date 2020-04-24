class Solution:

    # need to remove the duplicates in-place
    # need two pointer

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique = 1

        for i in range(len(nums)-1):

            if nums[i] < nums[i+1]:
                #when found a unique value
                nums[unique] = nums[i+1]
                unique += 1

        # delete elements after the last unique element
        del nums[unique:]
        return unique
