def solution(A):
    # write your code in Python 3.6
    min_avg = sum(A[:2]) / 2
    start_i = 0

    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            s_avg = sum(A[i:j+1])/(j-i+1)
            if s_avg < min_avg:
                min_avg = s_avg
                start_i = i

    return start_i


def solution2(A):
    min_avg = 10001
    start_i = -1

    for i in range(len(A)-1):
        s2_avg = (A[i] + A[i+1]) / 2
        if s2_avg < min_avg:
            min_avg = s2_avg
            start_i = i
        
        if i < len(A)-2 :
            s3_avg = (A[i] + A[i+1] + A[i+2]) / 3
            if s3_avg < min_avg:
                min_avg = s3_avg
                start_i = i

    return start_i




print(solution2([4,2,2,5,1,5,8]))