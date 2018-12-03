def solution(A):
    diff_left = sum(A[:1])
    diff_right = sum(A[1:])
    d_min = abs(diff_left - diff_right)

    for i in range(1, len(A)-1):
        diff_left = diff_left + A[i]
        diff_right = diff_right - A[i]

        d_min = min(d_min, abs(diff_left - diff_right))

        # min_diff = min(abs(sum(A[:i+1]) - sum(A[i+1:])), min_diff)
    
    return d_min




print(solution([-1000, 1000]))