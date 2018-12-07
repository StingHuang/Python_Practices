def solution(A):
    if len(A) == 0:
        return -1

    candi = sorted(A)[len(A)//2]
    count = 0
    c_index = []
    
    for i in range(len(A)):
        if A[i] == candi:
            count += 1
            c_index.append(i)
    
    if count > len(A)//2:
        return c_index[0]
    else:
        return -1


A = [3, 4, 3, 2, 3, -1, 3, 3]
print(solution(A))