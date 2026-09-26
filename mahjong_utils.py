"""Shared hand traversal helpers, independent of the display."""
def next_two_not_block(block, mj_num, next):
    n0 = next_not_block(block, mj_num, next)
    if -1 == n0:
        return -1, -1
    n1 = next_not_block(block, mj_num, n0+1)
    if -1 == n1:
        return n0, -1

    return n0, n1

def next_two_not_blsame(block, mj_num, next, mj, sv):
    n0 = next_not_blsame(block, mj_num, mj, sv, next)
    if -1 == n0:
        return -1, -1
    n1 = next_not_blsame(block, mj_num, mj, mj[n0], n0+1)
    if -1 == n1:
        return n0, -1

    return n0, n1

# return -1 if exceed mj_num
def next_not_block(block, mj_num, next=0):
    i = next
    while i < mj_num:
        if 0 == block[i]:
            return i
        i += 1

    return -1

# return -1 if exceed mj_num
def next_not_blsame(block, mj_num, mj, sv, next=0):
    i = next
    while i < mj_num:
        if 0 == block[i] and mj[i] != sv:
            return i
        i += 1

    return -1

