def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    k = sorted(nums)
    s = 0
    for i in range(0,len(k),2):
        s += min(k[i],k[i+1])
    return s