import sys

def is_adjacent(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) + abs(y1 - y2) == 1

def dfs(coordinate_set):
    visited = set()  # 방문한 좌표를 저장하는 집합
    groups = []      # 좌표 그룹을 저장하는 리스트

    def explore(coord, group):
        visited.add(coord)
        group.add(coord)

        for neighbor in coordinate_set:
            if neighbor not in visited and is_adjacent(coord, neighbor):
                explore(neighbor, group)

    for coordinate in coordinate_set:
        if coordinate not in visited:
            new_group = set()
            explore(coordinate, new_group)
            groups.append(new_group)

    return sorted([len(group) for group in groups])  # 그룹 크기를 오름차순 정렬하여 반환

if __name__ == '__main__':
    N, M, K = map(int, sys.stdin.readline().rstrip().split())
    empty_area_coordinates_set = set()
    
    for _ in range(K):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
        for y in range(y1, y2):
            for x in range(x1, x2):
                empty_area_coordinates_set.add((x, y))

    groups = dfs(empty_area_coordinates_set)
    print(len(groups))
    print(*groups)
