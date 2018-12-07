def solution(A):
    n = len(A)
    result = -float("inf")
    for i in range(n):
        slice_sum = 0
        for j in range(i, n):
            slice_sum += A[j]
            result = max(result, slice_sum)

    return result

def solution_2(A):
    maxEndingHere = A[0]
    maxSoFar = A[0]
    for i in range(1, len(A)):
        maxEndingHere = max(A[i], maxEndingHere + A[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    
    return maxSoFar



A = [3,2,-6,4,0]
print(solution_2(A))
