def solution(routes):
    answer = 1
    routes.sort(key=lambda x: x[1])
    camera_loc = routes[0][1]
    
    if len(routes) == 1:
        return answer
    
    for enterance, exit in routes[1:]:
        if camera_loc < enterance:
            answer+=1
            camera_loc = exit

    return answer

 