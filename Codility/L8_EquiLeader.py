def solution(A):
    count = 0

    for i in range(1, len(A)):
        # print("{} -- {}".format(A[:i], A[i:]))

        left = sorted(A[:i])
        left_leader = left[(i//2)]

        if (len(left) == 2) or (left.count(left_leader) < (len(left)//2)+1):
            continue
      
        # print("left_leader: {}".format(left_leader))

        right = sorted(A[i:])
        right_leader = right[(len(A)-i)//2]
        if (len(right) == 2) or (right.count(right_leader) < (len(right)//2)+1):
            continue
        else:
            # print("right_leader: {}".format(right_leader))
            if left_leader == right_leader:
                count += 1

    return count


from itertools import groupby
def solution2(A):
    d = dict()
    key = value = -1
    maxGroup = max(groupby(sorted(A)), key = lambda x: len(list(x[1])))
    key = maxGroup[0]
    value = len(list(filter(lambda x: x == key, A)))

    length = len(A)
    if value <= length / 2:
        return 0

    left = 0
    right = value
    count = 0
    for i in range(length):
        if A[i] == key:
            left  += 1
            right -= 1

        if left > (i+1) / 2 and right > (length - i - 1) / 2:
            count += 1

    return count

A = [4,3,4,4,4,2]
print(solution2(A))