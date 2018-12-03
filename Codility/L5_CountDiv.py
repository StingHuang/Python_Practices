def solution(A, B, K):
    count = 0
    for num in range(A, B+1):
        if num % K == 0:
            count += 1
    
    return count


def solution2(A, B, K):
    count = (B // K) - (A // K)
    if A % K == 0:
        count += 1
    
    return count



print(solution2(11, 345, 17))