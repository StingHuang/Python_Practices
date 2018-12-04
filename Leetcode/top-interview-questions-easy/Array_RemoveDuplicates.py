class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        if len(nums) > 0:
            count += 1
            for i in range(1, len(nums)):
                if nums[i] != nums[i-1]:
                    count += 1
                    nums[count-1] = nums[i]
        return count


s = Solution()
test = [1,1,2,2,3,3,3,5,6,6]
print(s.removeDuplicates(test))