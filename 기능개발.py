def solution(progresses, speeds):
    answer = []         #result_cnt
    result_days = [] 
    n = 0       #n일째
    start = 0   #return_list의 인덱스, 연속을 확인하기 위함
    new_progresses = [0 for i in range(len(progresses))] 
    
    while new_progresses != [-1 for i in range(len(progresses))]: 
        for i in range(start, len(progresses)):
                new_progresses[i] = progresses[i] +speeds[i] * n
        
        cnt = 0
        for j in range (start, len(new_progresses)):
            if new_progresses[j] >= 100:
                cnt += 1
                new_progresses[j] = -1
            else:
                start = j
                break
                
        if cnt > 0:
            result_days.append(n)
            answer.append(cnt)
              
        n += 1 
        
    return answer
