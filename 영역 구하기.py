import sys
# 전체 - 직사각형 => 빈 좌표 집합
def sorting_empty_coordinate_set(m,n,k):
    false_set, true_set = set(), set()
    for _ in range(k):
        x1,y1, x2,y2 = map(int, sys.stdin.readline().rstrip().split())
        for y in range(y1,y2):
            for x in range(x1,x2):
                false_set.add((x,y))
    for y in range(0,n):
        for x in range(0,m):
            true_set.add((x,y))
    return true_set - false_set
# dfs로 풀기 위해 인접 노드 딕셔너리 만들기
def set_to_adj_dic(coor_set):
    coor_dic, coor_adj_dic = dict(), dict()
    for xy in coor_set:
        coor_dic[xy] = True
    for xy in coor_set:
        tm_adj_list = []
        if coor_dic.get((xy[0]+1,xy[1]), False): tm_adj_list.append((xy[0]+1,xy[1]))
        if coor_dic.get((xy[0]-1,xy[1]), False): tm_adj_list.append((xy[0]-1,xy[1]))
        if coor_dic.get((xy[0],xy[1]+1), False): tm_adj_list.append((xy[0],xy[1]+1))
        if coor_dic.get((xy[0],xy[1]-1), False): tm_adj_list.append((xy[0],xy[1]-1))
        coor_adj_dic[xy] = tm_adj_list
    return coor_adj_dic, coor_dic
# dfs로 풀기
# 처음에 list형식 사용했다가 시간초과로 set으로 바꿈
# set = 해시 O(1), list = 동적 배열 O(n)
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
    result,sol = [],[]
    N,M,K = map(int, sys.stdin.readline().rstrip().split())
    adj_dic, coor_dic = set_to_adj_dic(sorting_empty_coordinate_set(M,N,K))
    
    while coor_dic:
        tm = coor_dic.popitem()
        sol = dfs(adj_dic, tm[0], coor_dic)
        result.append(len(sol))
    print(len(result))
    sys.stdout.write(' '.join(map(str,sorted(result))))