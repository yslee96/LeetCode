class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0 for _ in range(len(rooms))]
        def dfs(room_number):
            if visited[room_number]:
                return
            
            visited[room_number] = True
            for nxt_room in rooms[room_number]:
                dfs(nxt_room)
             
        dfs(0)
        return sum(visited) == len(rooms)