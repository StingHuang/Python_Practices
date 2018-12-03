def solution(A):
    # write your code in Python 3.6
    A.sort()
    pi = 0
    for i in range(len(A)):
        if A[i] > 0:
            pi = i
            break
    max_p1 = A[-1] * A[-2] * A[-3]
    if pi >= 2:
        max_c = A[0] * A[1] * A[-1]
        max_p1 = max(max_p1, max_c)

    return max_p1



print(solution([-10, -25, 8, 3, 2, 5]))