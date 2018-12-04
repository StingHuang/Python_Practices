def solution(A, B):
    count = 0
    stack = []

    for i in range(len(A)):
        n = A[i]
        # stack.append(n)
        if B[i] == 0:
            while stack:
                if stack[-1] < n:
                    stack.pop()
                else:
                    break
            if not stack:
                count += 1

        elif B[i] == 1:
            stack.append(n)
    
    count = count + len(stack)
    return count


A = [3,2,6,1,5,4]
B = [1,1,0,0,1,0]
print(solution(A, B)) # return 3