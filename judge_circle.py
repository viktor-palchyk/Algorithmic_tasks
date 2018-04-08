def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    ups = downs = lefts = rights = 0
    ups = moves.count("U")
    downs = moves.count("D")
    lefts = moves.count("L")
    rights = moves.count("R")
    if ups - downs == lefts - rights:
        return True
    else:
        return False
    # 657 leetcode