# class Solution:
#     def twoSum(self, nums, target):
#         xtr = 1
#         for i in range(len(nums)-1):
#             for y in range(len(nums)-1):
#                 if i == y+1:
#                     continue
#                 elif nums[i]+nums[y+1] == target:
#                     return [i,y+1]
#
#
#
# nums = [2,7,11,15]
#
#
# target = 9
#
#
#
# p = Solution()
#
# q = p.twoSum(nums,target)
# print(q)


# Best approach given below :

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            print(f'i = {i}  , '
                  f'num = {num}')
            n = target - num
            print("n ---- >",{n})

            if n not in h:
                h[num] = i
                print(f'blk 1 ---->n = {n} , h = {h}')
            else:
                print(f'n = {n} , h = {h}')
                return [h[n], i]


nums = [3,7,5,4,9,11,46,70,2]
target = 5

p = Solution().twoSum(nums,target)
print(p)
