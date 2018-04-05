def moveZeroes(self, nums):
    nums.sort(key=lambda v: v == 0)
    # 283 task on leetcode.com