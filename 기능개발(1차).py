def solution(progresses, speeds):
    return_list = [0 for i in range(len(progresses))] 
    answer = [] 
    result_day = [] 
    n = 1 
    proN = 0 
    
    while(return_list != [1 for i in range(len(progresses))]): 
        new_progresses = [] 
        for i in range(len(progresses)):
            new_progresses.append(progresses[i] +speeds[i] * n) 
        
        for j in range(len(new_progresses)): 
            if (new_progresses[j] >= 100): 
                return_list[j] = 1 
                progresses[j] = -1
                speeds[j] = 0
                
        if (return_list[proN] == 1):
            cnt = 0
            for k in range(proN, len(return_list)):
                if (return_list[k] == 1): 
                    cnt += 1 
                else: 
                    break
                    
            result_day.append(n) 
            answer.append(cnt) 
            proN = k 
              
        n += 1 
        
    return answer
