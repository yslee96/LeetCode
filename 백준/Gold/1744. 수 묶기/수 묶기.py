import sys
input = sys.stdin.readline
total_nums = int(input())
plus, minus = [], []
num_zeros = 0

if total_nums < 2:
    print(int(input()))
else:
        
    for i in range(total_nums):
        num = int(input())
        if num > 0:
            plus.append(num)
        elif num < 0:
            minus.append(num)
        else:
            num_zeros +=1
    
    plus.sort(reverse=True)
    minus.sort()
    
    total_sum = 0
    num_pluses = len(plus)
    for i in range(0, num_pluses, 2):
        if i+1 >= num_pluses: break 
        total_sum += max(plus[i]+plus[i+1], plus[i] * plus[i+1])
    
    if num_pluses % 2:
        total_sum += plus[-1]
    
    num_minuses = len(minus)
    for i in range(0, num_minuses, 2):
        if i+1 >= num_minuses: break 
        total_sum += max(minus[i]+minus[i+1], minus[i] * minus[i+1])
        
    if num_minuses % 2:
        total_sum += 0 if num_zeros else minus[-1]
    
    print(total_sum)