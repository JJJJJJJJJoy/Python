class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       
      dic = {}
      for i , value in enumerate(nums):
          r = target - nums[i]

          if r in dic:
              return[i, dic[r]]

          dic[value] = i

