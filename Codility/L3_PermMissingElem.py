def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1

    A.sort()
    for i in range(len(A)):
        if A[0] != 1:
            return 1
        elif A[len(A)-1] != len(A)+1:
            return len(A)+1
        
        if A[i] != i+1:
            return i+1

print(solution([3,2]))