class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left_right_heights = []
        if len(height) < 3:
            return water
        else:
            for i in range(1, len(height) - 1):
                left_right_heights.append([height[i - 1], height[i], height[i + 1]])

            print left_right_heights

            for heights in left_right_heights:
                if (min(heights[0], heights[2]) - heights[1]) > 0:
                    water += (min(heights[0], heights[2]) - heights[1]) * 1
            return water

if __name__ == '__main__':
    print Solution().trap([2,1,0,2])