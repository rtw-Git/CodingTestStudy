def solution(participant, completion):
    answer = ''
    
    participant.sort()      #정렬부터
    completion.sort()
    
    for i in range (len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        answer = participant[i+1]       #완주하지 못한 선수가 참여자 명단 맨 마지막에서 발견
        
    return answer
