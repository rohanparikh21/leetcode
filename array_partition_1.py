class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums = sorted(nums)
        j = len(nums) - 1
        for i in range(len(nums)):
            sum = sum + (nums[j] - nums[i])
            j -= (i+1)
            if j < i:
                break
        return sum

if __name__ == '__main__':
    print Solution().arrayPairSum([1,4,3,2])