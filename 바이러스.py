import sys
import collections

def virus(adj_dic):
    bfs_visited = {k : False for k in adj_dic}  # 노드 방문여부
    bfs_visit_list = []                         # 방문한 결과 
    bfs_deque = collections.deque()             # 큐

    def bfs(node):
        bfs_visited[node] = True    
        bfs_visit_list.append(node)
        for i in adj_dic[node]:
            adj_node = i
            if bfs_visited[adj_node] == False and not adj_node in bfs_deque:
                bfs_deque.appendleft(adj_node)
        if bfs_deque:
            bfs(bfs_deque.pop())
        return
    
    bfs(1)
    return bfs_visit_list

if __name__ == '__main__':
    n = int(input())
    n = int(input())
    adjac_dic = dict()
    # 인접 노드 딕셔너리 만들기
    for _ in range(n):
        node1, node2 = map(int, sys.stdin.readline().split())
        if node1 in adjac_dic:
            adjac_dic[node1].append(node2)
        else:
            adjac_dic[node1] = [node2]
        if node2 in adjac_dic:
            adjac_dic[node2].append(node1)
        else:
            adjac_dic[node2] = [node1]
    # 간선이 0개 일때 처리
    try:
        tm_list = virus(adjac_dic)
        print(len(tm_list)-1)
    except:
        print(0)