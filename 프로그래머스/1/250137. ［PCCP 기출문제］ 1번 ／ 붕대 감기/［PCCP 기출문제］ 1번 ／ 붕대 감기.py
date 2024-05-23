from collections import deque
def solution(bandage, max_health, attacks):
    answer = 0    
    duration, heal_per_sec, heal_additional = bandage

    attacks = deque(attacks)
    health = max_health
    cur_time = 0   
    while attacks:
        attack_time, attack_damage = attacks.popleft()
        serial = 0
        for t in range(cur_time+1, attack_time):
            health = min(max_health, health + heal_per_sec)
            serial +=1
            if serial == duration:
                health = min(max_health, health + heal_additional)
                serial = 0
        
        if health <= attack_damage:
            health = -1
            break
            
        health -= attack_damage
        cur_time = attack_time
            
    return health
            

    

        
        
    return answer