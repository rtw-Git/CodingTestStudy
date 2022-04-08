def solution(n):
    answer = 0
    
    for i in range (1, n):      #1과 n으로 나누면 나머지 0이니 범위는 2 ~ n-1
        if n%i == 1:
            answer = i
            break
                
    return answer
