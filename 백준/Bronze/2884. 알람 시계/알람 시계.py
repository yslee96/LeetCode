import sys
input = sys.stdin.readline
hour, minutes = map(int, input().split())
mod = 60 * 24
cur_minutes = hour * 60 + minutes
alarm_minutes = (cur_minutes - 45) % mod
alarm_hour, alarm_minutes = alarm_minutes // 60, alarm_minutes % 60
print(alarm_hour, alarm_minutes)
