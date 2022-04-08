def solution(progresses, speeds):
    return_list = [0 for i in range(len(progresses))] 
    answer = []         #result_cnt
    result_day = [] 
    n = 1       #n일째
    start = 0   #return_list의 인덱스, 연속을 확인하기 위함
    
    while return_list != [1 for i in range(len(progresses))]: 
        new_progresses = [0 for i in range(len(progresses))] 
        for i in range(len(progresses)):
            if new_progresses[i] != -1:
                new_progresses[i] = progresses[i] +speeds[i] * n
        
        for j in range(len(new_progresses)): 
            if (new_progresses[j] >= 100): 
                return_list[j] = 1 
                new_progresses[j] = -1
                
        if (return_list[start] == 1):
            cnt = 0
            for k in range(start, len(return_list)):
                if (return_list[k] == 1):   #완성이 성립 시 +1(완성 기능)
                    cnt += 1 
                else:                       #미완성이면 반복문 나감
                    break
                    
            result_day.append(n) 
            answer.append(cnt) 
            start = k                       #다음날에 이어서 완성이 되는지 확인하기 위함
              
        n += 1 
        
    return answer
