def solution(n, wires):
    answer = -1
    start_node = wires[0][0]
    
    node = dict()
    sub_nodes_cnt = dict()
    for w in wires:
        sub_nodes_cnt[w[0]] = 0
        sub_nodes_cnt[w[1]] = 0
        if w[0] in node:
            node[w[0]].append(w[1])
        else:
            node.update({w[0]:[w[1]]})
        if w[1] in node:
            node[w[1]].append(w[0])
        else:
            node.update({w[1]:[w[0]]})

    tm = [-1]
    tree_node = dict()
    #자식 노드 개수
    def cal_sub_node(nd):    
        for d in node[nd]:
            t = tm.pop()
            if d != t:
                print(d, nd)
                if nd in tree_node:
                    tree_node[nd].append(d)
                else:
                    tree_node[nd] = [d]
                sub_nodes_cnt[nd] += 1
                tm.append(nd)
                cal_sub_node(d)
            else:
                tm.append(t)
        return
    
    cal_sub_node(start_node)

    total_sub_node_cnt = []
    print(tree_node)
    print(sub_nodes_cnt)

    for node in reversed(tree_node):
        total = 0
        for sub_n in tree_node[node]:
            total += 1 if sub_nodes_cnt[sub_n] == 0 else sub_nodes_cnt[sub_n]
        sub_nodes_cnt[node] = (total + 1)
        print(node, sub_nodes_cnt[node])
        total_sub_node_cnt.append(sub_nodes_cnt[node])

    print(total_sub_node_cnt)
    average = total_sub_node_cnt[-1]/2
    big = 0
    sml = 0
    for cnt in total_sub_node_cnt:
        if cnt < average:
            print(cnt, 1)
            sml = cnt
        else:
            print(cnt, 2)
            big = cnt
            break
    
    return big - sml
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
n = 9
print(solution(n, wires))