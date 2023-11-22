import sys
from collections import defaultdict
from heapq import heappop, heappush
input = sys.stdin.readline

num_cities, num_cables, num_plants = map(int, input().split())
costs = [[0 for _ in range(num_cities+1)] for _ in range(num_cities+1)]
has_plant = defaultdict(int)
rep_of_city = [i for i in range(num_cities+1)]
num_reps = num_cities
city_with_plants = list(map(int, input().split()))
pq = []
min_total_cost = 0
for city in city_with_plants:
    has_plant[city] = 1
for _ in range(num_cables):
    city1, city2, cost = map(int, input().split())
    heappush(pq, [cost, city1, city2])

def find_rep(city):
    if rep_of_city[city] == city:
        return city
    rep_of_city[city] = find_rep(rep_of_city[city])
    return rep_of_city[city]

def is_same_set(city1, city2):
    return find_rep(city1) == find_rep(city2)

def union_set(city1, city2):
    rep_of_city[city2] = city1
    
while num_reps > num_plants:
    cur_cost, c1, c2 = heappop(pq)
    if not is_same_set(c1, c2):
        r1, r2 = find_rep(c1), find_rep(c2)
        if has_plant[r1] and has_plant[r2]:
            continue
        elif has_plant[r1] and not has_plant[r2]:
            union_set(r1, r2)
        elif has_plant[r2] and not has_plant[r1]:
            union_set(r2, r1)
        else:
            union_set(r1,r2)
        min_total_cost += cur_cost
        num_reps-=1
        
print(min_total_cost)