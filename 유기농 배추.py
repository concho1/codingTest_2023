import sys
def in_to_adj_dic():
    cabbage_xy_dic, cabbage_adj_dic = dict(), dict()
    row, column, cabbage_cnt = map(int, sys.stdin.readline().rstrip().split())
    # dfs하기 위해 인접 노드 딕셔너리 만들기
    for _ in range(cabbage_cnt):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        cabbage_xy_dic[(x,y)] = True
    for xy in cabbage_xy_dic:
        tm_adj_list = []
        if cabbage_xy_dic.get((xy[0]+1,xy[1]), False): tm_adj_list.append((xy[0]+1,xy[1]))
        if cabbage_xy_dic.get((xy[0]-1,xy[1]), False): tm_adj_list.append((xy[0]-1,xy[1]))
        if cabbage_xy_dic.get((xy[0],xy[1]+1), False): tm_adj_list.append((xy[0],xy[1]+1))
        if cabbage_xy_dic.get((xy[0],xy[1]-1), False): tm_adj_list.append((xy[0],xy[1]-1))
        cabbage_adj_dic[xy] = tm_adj_list
    return cabbage_adj_dic, cabbage_xy_dic
    
def dfs(graph, start, coor_dic):
    result, visit = set(), []
    visit.append(start)

    while visit:
        node = visit.pop()
        if node not in result:
            result.add(node)
            visit.extend(graph[node])
            coor_dic.pop(node,0)
    return result

if __name__ == '__main__':
    test_case = int(input())
    total = []
    for _ in range(test_case):
        result,sol = [],[]
        adj_dic, coor_dic = in_to_adj_dic()
        while coor_dic:
            tm = coor_dic.popitem()
            sol = dfs(adj_dic, tm[0], coor_dic)
            result.append(len(sol))
        total.append(len(result))
    for t in total:
        print(t)