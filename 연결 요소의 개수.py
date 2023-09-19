# BFS로 안풀고 집합으로 풀어보기
import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().strip().split())
    # 간선이 없을때 처리
    if m == 0:
        print(n)
        exit()
    # 리스트와 집합 형식으로 받기
    node_list, node_lset, total_node_set, cnt = [], [], set(), 1
    for _ in range(m):
        tm = list(sorted(map(int, sys.stdin.readline().strip().split())))
        node_list.append(tm)
        total_node_set.update(tm)
    node_list.sort(key= lambda x:(x[0]))
    # 두 숫자가 기존 집합에 없으면 새로운 집합을 만든다.
    node_set = set(node_list[0])
    for i in range(1, m):
        if not (node_list[i][0] in node_set or node_list[i][1] in node_set):
            cnt += 1
            node_lset.append(node_set.copy())
            node_set.clear()
        node_set.update(node_list[i])
    node_lset.append(node_set.copy())
    # 교집합 검사
    for i in range(len(node_lset)):
        for j in range(i+1, len(node_lset)):
            if node_lset[i] & node_lset[j] != set():
                cnt -= 1
    
    print(cnt - len(total_node_set) + n)