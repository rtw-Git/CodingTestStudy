def solution(s):
    answer = True
    stack = []
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    
    for i in s:
        if i == '(':                #'('일 때만 값을 넣게 함
            stack.append(i)
        else:                       #')'일 때는
            if stack == []:         #stack이 비어있으면 앞에 '('가 없다는 말이므로 False
                return False
            else:                   #stack이 비어있지 않으면 앞에 '('가 있다는 말이므로 마지막 '(' 제거
                stack.pop()

    if stack != []:                 #s를 다 돌았는데 stack이 비어있지 않으면 '('가 남는다는 말이므로 False
        return False

    return True                     #나머지의 경우는 다 True
