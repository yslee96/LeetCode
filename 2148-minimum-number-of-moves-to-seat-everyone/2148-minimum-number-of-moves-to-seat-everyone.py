class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(map(lambda x: abs(x[1]-x[0]), zip(sorted(seats), sorted(students))))