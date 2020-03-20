def makeArrayConsecutive2(statues):
    statues.sort()
    if len(statues) > 1:
        diff_statues = [y-x for x, y in zip(statues[:-1], statues[1:])]
        return sum(i-1 for i in diff_statues)
    else:
        return 0
makeArrayConsecutive2(statues=[1,2,3,4,5])