def thirdMax(self, nums):
    s = list(set(nums))
    k = sorted(s, reverse=True)
    if len(k) < 3:
        return max(k)
    else:
        return k[2]
    #414 task on leetcode.com