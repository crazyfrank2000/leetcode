#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers, target: int):
       i = 0
       j= len(numbers)-1
       sum = 0
       
       while i < j:
           sum = numbers[i] + numbers[j]
           if sum == target :
               return [i+1, j+1]
           elif sum < target: 
              i=i+1
           else:
              j=j-1
              
       return [-1,-1]
# @lc code=end
            
            
