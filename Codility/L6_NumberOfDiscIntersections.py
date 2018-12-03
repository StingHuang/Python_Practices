def solution(A):
    range_list = []
    for i in range(len(A)):
        range_list.append((i-A[i], i+A[i]))
    
    count = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if (range_list[i][0] >= range_list[j][0]) and (range_list[i][0] <= range_list[j][1]):
                count += 1
            elif (range_list[i][1] >= range_list[j][0]) and (range_list[i][1] <= range_list[j][1]):
                count += 1
            elif (range_list[j][0] >= range_list[i][0]) and (range_list[j][0] <= range_list[i][1]):
                count += 1
            elif (range_list[j][1] >= range_list[i][0]) and (range_list[j][1] <= range_list[i][1]):
                 count += 1

    return count


def solution2(A):
    upper = sorted(([i+A[i] for i in range(len(A))]))
    lower = sorted(([i-A[i] for i in range(len(A))]))

    print("upper: {}".format(upper))
    print("lower: {}".format(lower))

    intersection = 0 # number of intersections
    j=0 # for the lower points

    for i in range(len(A)):
        print("upper[{}]: {}".format(i, upper[i]))
        while (j < len(A)) and (upper[i] >= lower[j]):
            print("lower[{}]: {}".format(j, lower[j]))
            intersection = intersection + j # add j intersections
            intersection = intersection - i #  minus "i" (avoid double count) 
            j += 1

    return intersection if intersection <= 10000000 else -1



print(solution2([1,5,2,1,4,0]))