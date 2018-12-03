def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
    for i in range(K):
        a = A.pop()
        A.insert(0, a)
    return A



print(solution([3, 8, 9, 7, 6], 3))