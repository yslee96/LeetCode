def solution(answers):
    solves = []
    answer = []
    
    def count_corrects(num, answers):
        
        results = [0 for _ in range(len(answers))]
        if num == 1:
            results = [1 if answers[i] == i%5 + 1 else 0 for i in range(len(answers))]
        elif num == 2:
            tmp = {1: 1, 3: 3, 5: 4, 7: 5}
            for i in range(len(answers)):
                if i%2 ==0:
                    results[i] = 1 if answers[i] == 2 else 0
                else:
                    results[i] = 1 if answers[i] == tmp[i%8] else 0
        else:
            tmp = [3,1,2,4,5]
            results = [1 if answers[i] == tmp[(i//2)%5] else 0 for i in range(len(answers))]
        #print(results)
        return sum(results)
    
    for num in range(1, 4):
        solves.append([count_corrects(num, answers), num])
    
    solves.sort(key=lambda x: (-x[0], x[1]))
    #print(solves)
    max_solves = -1
    for num_solves, num in solves:
        if num_solves < max_solves:
            break
        max_solves = num_solves
        answer.append(num)

    return answer