def solution(A):
    # write your code in Python 3.6
    A.sort()
    for i in range(0, len(A), 2):
        if i == len(A)-1:
            return A[i]
        if A[i] != A[i+1]:
            return A[i]
    '''
    for i in range(len(A)):
        if A[i] > 0:
            for j in range(i+1, len(A)):
                if A[i] == A[j]:
                    A[i] = 0
                    A[j] = 0
                    break
            if A[i] != 0: 
                return A[i]
    '''

print(solution([9, 3, 7, 3, 7]))  