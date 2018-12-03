def solution(N, A):
    cur_max = 0
    ans = [0] * N
    for i in range(len(A)):
        if A[i] <= N:
            ans[A[i]-1] += 1
            cur_max = max([ans[A[i]-1], cur_max])
        elif A[i] == N+1:
            ans = [cur_max] * N
    return ans


def solution2(N, A):
    last_max = 0
    cur_max = 0
    ans = [0] * N
    for i in range(len(A)):
        if A[i] <= N:
            ans[A[i]-1] = max([ans[A[i]-1], last_max])
            ans[A[i]-1] += 1
            cur_max = max([ans[A[i]-1], cur_max])
        elif A[i] == N+1:
            last_max = cur_max
    
    for j in range(len(ans)):
        ans[j] = max(ans[j], last_max)

    return ans


print(solution2(5, [3,4,4,6,1,4,4]))