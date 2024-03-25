import sys
input = sys.stdin.readline
string = input().rstrip()
str_len = len(string)
is_seen = [False for _ in range(str_len)]
def zoac(left, right):
  
  min_idx, min_ch = float('inf'), 'a'
  for idx in range(left, right):
    if is_seen[idx] == False and ord(string[idx]) < ord(min_ch):
      min_ch = string[idx]
      min_idx = idx
  
  if min_idx == float('inf'):
    return
  
  is_seen[min_idx] = True
  cur_str = '' 
  for i in range(str_len):
    if is_seen[i]:
      cur_str += string[i]
  
  print(cur_str)
  zoac(min_idx+1, right)
  zoac(left, min_idx)
  
zoac(0, str_len)