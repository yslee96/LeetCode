class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total_damage = sum(damage)
        answer = total_damage+1
        for i in range(len(damage)):
            answer = min(answer, total_damage+1 - min(damage[i], armor))
        return answer
        

        

