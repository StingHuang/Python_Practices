def maxArea(height):
    result = 0
    n = len(height)
    for i in range(n):
        area = 0
        for j in range(i, n):
            x = j - i
            y = min(height[j], height[i])
            area = x * y
            result = max(result, area)
    
    return result

def maxArea_2(height):
    max_result = 0
    head = 0
    tail = len(height) - 1
    while head < tail:
        x = tail - head
        y = min(height[tail], height[head])
        max_result = max(max_result, (x*y))
        if y == height[head]:
            head += 1
        else:
            tail -= 1
    
    return max_result



t_height = [1,8,6,2,5,4,8,3,7]
print(maxArea_2(t_height))