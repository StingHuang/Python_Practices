def sum_stack(stack):
    total_sum = int(stack[0])
    for j in range(1, len(stack), 2):
        if stack[j] == '+':
            total_sum = total_sum + int(stack[j+1])
        elif stack[j] == '-':
            total_sum = total_sum - int(stack[j+1])
    return total_sum

def calculate(s):
    stack = []
    for i in s:
        i = i.strip()
        if i != '':
            if i != ')':
                if len(stack) == 0 or stack[-1] in ['+', '-', '('] or i in ['+', '-', '(']:
                    stack.append(i)
                else:
                    stack.append((10 * int(stack.pop())) + int(i))
            elif i == ')':
                sub_stack = []
                sub_stack.insert(0, int(stack.pop()))
                last = stack.pop()
                while last != '(':
                    sub_stack.insert(0, last)
                    last = stack.pop()
                stack.append(sum_stack(sub_stack))
        print(stack)
    
    return sum_stack(stack)


S = "2-4-(8+2-6+(8+4-(1)+8-10))"
print(calculate(S))
