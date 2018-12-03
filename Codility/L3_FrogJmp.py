def solution(X, Y, D):
    distance = Y - X
    if distance % D != 0:
        return (distance // D) + 1
    else:
        return (distance // D)


print(solution(10, 85, 30))
