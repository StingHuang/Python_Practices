def solution(H):
    count = 0
    stack = []
    for n in H:
        while(stack and stack[-1] > n):
            stack.pop()
        if(stack and stack[-1] == n):
            continue
        stack.append(n)
        count += 1

    return count

print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))