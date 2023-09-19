import heapq

def solution(n, s, a, b, fares):
    answer = 0
    # 도로 제작(딕셔너리 형태)
    dic_moveable = {}
    set_node = set()
    for fare in fares:
        set_node.add(fare[0])
        set_node.add(fare[1])
        if fare[0] in dic_moveable:
            dic_moveable[fare[0]].update({fare[1]: fare[2]})
        else:
            dic_moveable[fare[0]] = {fare[1]: fare[2]}

        if fare[1] in dic_moveable:
            dic_moveable[fare[1]].update({fare[0]: fare[2]})
        else:
            dic_moveable[fare[1]] = {fare[0]: fare[2]}

    def dijkstra(graph, start):
        distance = {node: float('inf') for node in graph}
        distance[start] = 0
        
        queue = [(0, start)]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_distance > distance[current_node]:
                continue
            
            for neighbor, weight in graph[current_node].items():
                distance_to_neighbor = current_distance + weight
                
                if distance_to_neighbor < distance[neighbor]:
                    distance[neighbor] = distance_to_neighbor
                    heapq.heappush(queue, (distance_to_neighbor, neighbor))
        
        return distance

    # 다익스트라 알고리즘을 사용하여 특정 노드까지의 거리 계산
    s_distances = dijkstra(dic_moveable, s)
    a_distances = dijkstra(dic_moveable, a)
    b_distances = dijkstra(dic_moveable, b)
    tm = 0

    for node in set_node:
        tm = s_distances[node] + a_distances[node] + b_distances[node]
        if answer == 0 or answer > tm:
            answer = tm
    
    return answer

n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9], [4, 7, 1]]

solution(n, s, a, b, fares)