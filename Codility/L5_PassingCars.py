def solution(A):
    # write your code in Python 3.6
    count = 0
    for i in range(len(A)-1):
        if A[i] == 0:
            for j in range(i+1, len(A)):
                if A[j] == 1:
                    count += 1

    return count if count <= 1000000000 else -1


def solution2(A):
    num_z = 0
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            num_z += 1
        else:
            count = count + num_z

    return count if count <= 1000000000 else -1


print(solution2([0,1,0,1,1]))

