def numJewelsInStones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    c = 0
    for el in J:
        if el in S:
            c += S.count(el)
    return c
    # 771 on leetcode.com