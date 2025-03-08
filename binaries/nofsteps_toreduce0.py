# leetcode 1342 - number of steps to reduce a number to zero
def numberOfSteps(num: int) -> int:
    steps = 0
    while num > 0:
        if num&1:
            num-=1
        else:
            num>>=1
        steps+=1
    return steps