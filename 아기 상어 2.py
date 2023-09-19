# 아기 상어에서 출발해서 빈칸까지의 거리는 
# 아기 상어를 기준으로 정사각형을 그리면서 탐색한다면 쉽게 구할 수 있다.
import sys
def input_cal():
    nm_map, xy_list, map_dic = [], [], dict()
    N, M = map(int, sys.stdin.readline().strip().split())
    for _ in range(N):
        nm_map.append(list(map(int, sys.stdin.readline().strip().split())))
    # 아기 상어들의 좌표를 찾고 -1로 바꿔준다 + 좌표 딕셔너리 맵을 만든다.
    for i in range(N):
        for j in range(M):
            if nm_map[i][j] == 1:
                nm_map[i][j] = -1
                xy_list.append([j,i])
            else:
                nm_map[i][j] = 100 #빈칸이 0이면 if문에서 False처리하므로 100기본값으로
            map_dic[(j,i)] = nm_map[i][j]
    return xy_list, map_dic, N, M

def square_search(x, y, map_dicl, Nl, Ml):
    x -=1
    y -=1
    square_size, break_point, cnt, max_size = 2, False, 1, max(Nl, Ml)
    while cnt < max_size:
        # 북
        for _ in range(square_size):
            x += 1
            tm = map_dicl.get((x,y),-2)
            if tm != -2:
                map_dicl[(x,y)] = cnt if tm > cnt else tm
        # 동
        for _ in range(square_size):
            y += 1
            tm = map_dicl.get((x,y),-2)
            if tm != -2:
                map_dicl[(x,y)] = cnt if tm > cnt else tm
        # 남
        for _ in range(square_size):
            x -= 1
            tm = map_dicl.get((x,y),-2)
            if tm != -2:
                map_dicl[(x,y)] = cnt if tm > cnt else tm
        # 서
        for _ in range(square_size):
            y -= 1
            tm = map_dicl.get((x,y),-2)
            if tm != -2:
                map_dicl[(x,y)] = cnt if tm > cnt else tm
        x -=1
        y -=1
        cnt += 1
        square_size += 2
    return

if __name__ == '__main__':
    xy_listm, map_dicm, Nm, Mm = input_cal()
    for x_y in xy_listm:
        square_search(x_y[0], x_y[1], map_dicm, Nm, Mm)
    sol = 1
    for i in range(Nm):
        for j in range(Mm):
            if map_dicm[(j,i)] > sol:
                sol = map_dicm[(j,i)]
    print(sol)