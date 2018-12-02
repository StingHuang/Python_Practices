def solution(S, P, Q):
    impact_factor = [("A", 1), ("C", 2), ("G", 3), ("T", 4)]
    ans = []

    for i in range(len(P)):
        sub_s = S[P[i]:Q[i]+1]
        for k in range(len(impact_factor)):
            if impact_factor[k][0] in sub_s:
                ans.append(impact_factor[k][1])
                break
    
    return ans




print(solution("CAGCCTA", [2,5,0], [4,5,6]))