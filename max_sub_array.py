class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            mid = (0 + len(nums))/2
            return max(sum(nums), self.maxSubArray(nums[:mid]), self.maxSubArray(nums[mid:]), self.maxSubArray(mu\
                                                                                                    ))

if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray(arr)
    # mid = (0+len(arr))/2
    # print arr[:mid], arr[mid:]
    pass