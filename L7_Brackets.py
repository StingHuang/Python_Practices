def solution(S):

    s_stack = []
    for i in range(len(S)):
        if S[i] == "(" or S[i] == "[" or S[i] == "{":
            s_stack.append(S[i])
        else:
            if len(s_stack) <= 0:
                return 0

            pop_s = s_stack.pop()
            if S[i] == ")" and pop_s == "(":
                continue
            elif S[i] == "]" and pop_s == "[":
                continue
            elif S[i] == "}" and pop_s == "{":
                continue
            else:
                return 0

    return 1 if len(s_stack) == 0 else 0





print(solution("{[()()]}"))
print(solution(")("))