def missingNumber(self, nums):
        n = len(nums)
        return int(n * (n+1) / 2 - sum(nums))
        #268 task on leetcode.com