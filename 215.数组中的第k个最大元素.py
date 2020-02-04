#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums, k):
        return self.quick_sort(nums,k)
    
    def partition(self,nums,left,right):
        # divde the array into left and right   
        while True:
            while nums[left]<nums[right]:
                right -= 1
            else:
                nums[left],nums[right]=nums[right],nums[left]
                if left >= right:
                    break
                left += 1
                
            while nums[left] < nums[right]:
                left += 1
            else:
                nums[left],nums[right]=nums[right],nums[left]
                if left >= right:
                    break
                right -= 1
        return left
            
    def quick_sort(self,nums,k):
        k = len(nums)-k
        left = 0
        right = len(nums) -1
        while left < right :
            j = self.partition(nums,left,right)
            if j == k:
                break
            elif j < k:
                left = j + 1
            else:
                right = j - 1
        return nums[k]
    # @lc code=end

