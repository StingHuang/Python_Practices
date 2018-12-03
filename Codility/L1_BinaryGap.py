# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    
    int_b = int("{0:b}".format(N))
    print('{}: {}'.format(N, int_b))
    '''
    len(max(format(N, 'b').strip('0').split('1')))
    
    gap = [0,]
    begin = False
    result = 0
    while int_b > 0:

        if int_b % 10 == 0:
            int_b /= 10
            if begin:
                result += 1

        elif int_b % 10 == 1:
            int_b = (int_b - 1) / 10
            if begin:
                if result > 0:
                    begin = False
                    gap.append(result)
                    if int_b > 0:
                        begin = True
                        result = 0
            else:
                begin = True

    print(gap)
    '''
    return len(max(format(N, 'b').strip('0').split('1')))


print(solution(1041))