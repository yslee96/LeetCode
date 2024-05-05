def solution(brown, yellow):
    answer = []
    yellow_w = yellow
    yellow_h = 0
    while yellow_w >= yellow_h:
        yellow_h+=1
        if yellow % yellow_h !=0:
            continue
        yellow_w = yellow / yellow_h
        brown_w, brown_h = yellow_w+2, yellow_h+2
        total_brown = brown_w*2 + brown_h*2 - 4
        if total_brown == brown:
            answer = [brown_w, brown_h]
            break
    
    return answer