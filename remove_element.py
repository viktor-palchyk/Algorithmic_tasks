def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    l = len(nums)
    while i < l:
        if val in nums:
            del nums[nums.index(val)]
        i += 1
    # 27