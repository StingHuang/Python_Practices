def solution(A):
    A.sort()
    cur = 0
    for i in range(len(A)):
        if A[i] == cur + 1 or A[i] == cur:
            cur = A[i] if A[i] > 0 else 0
        elif A[i] - cur > 1:
            return cur + 1
    return cur + 1


print(solution([2, 1, 3, 6]))