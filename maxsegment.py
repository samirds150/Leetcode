# write a function for given an array of A of N integers, returns the maximum number of segments of length 2, such that the segment has an equal sum

# for example, given A = [4, 3, 4, 4, 4, 2], the function should return 3, because we can find three segments of length 2, such that the segment has an equal sum, for example, (4, 3), (4, 4) and (4, 4)





s = [10, 1, 3, 1, 2, 2, 1, 0, 4]

def solution(s):
    d = {}
    l =[]
    for i in range(len(s)-1):
        if s[i] or s[i+1] not in l:
            sum = s[i] + s[i+1]
            l.append(i)
            l.append(i+1)
            print(l)
            if sum in d:
                d[sum] += 1
            else:
                d[sum] = 1
    print(d)
    return max(d.values())

solution(s)