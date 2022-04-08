def solution(n, m):
    answer = []
    
    i = n
    while i>0:
        if n%i == 0 and m%i == 0:
                answer.append(i)
                break
        i -= 1
    
    check = 0
    for j in range (1, m+1):
        for k in range (1, n+1):
            if n*j == m*k:
                answer.append(n*j)
                check = 1
                break
        if check == 1:
            break
                
    return answer
