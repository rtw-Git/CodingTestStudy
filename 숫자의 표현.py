def solution(n):
    answer = 0
    
    for i in range (1, n+1):
        s = 0
        for j in range (i, n+1):
            s += j
            if s<n:
                continue        #계속 더함
            if s==n:
                answer += 1
            if s>n:
                break           #끝내버림
            
    return answer
