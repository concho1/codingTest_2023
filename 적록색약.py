import sys
def solution():
    def get_adj(char_map_dic, x, y, tm_ch): # 인접한 색 탐색
        tm_adj_xy = []
        if char_map_dic.get((x-1,y), False) == tm_ch: tm_adj_xy.append((x-1,y))
        if char_map_dic.get((x+1,y), False) == tm_ch: tm_adj_xy.append((x+1,y))
        if char_map_dic.get((x,y-1), False) == tm_ch: tm_adj_xy.append((x,y-1))
        if char_map_dic.get((x,y+1), False) == tm_ch: tm_adj_xy.append((x,y+1))
        return tm_adj_xy
    
    def dfs(dic_map): # dfs 
        dic_map_keys = set(dic_map.keys())
        result = []
        while dic_map_keys:
            start = dic_map_keys.pop()
            visited, visit = set(), []
            visit.append(start)
            while visit:
                node = visit.pop()
                if node not in visited:
                    visited.add(node)
                    visit.extend(dic_map[node])
                    dic_map_keys.discard(node)
            result.append(visited)
        
        return result

    char_map_dic, color_blindness_dic = dict(), dict()
    n = int(input())
    for y in range(n):
        for x, ch in enumerate(sys.stdin.readline().rstrip()):
            char_map_dic[(x,y)] = ch
            color_blindness_dic[(x,y)] = 'R' if 'G' == ch else ch

    # 인접 노드 딕셔너리를 R, G, B, RorG 4개 만들어 준다.
    r_dic, g_dic, b_dic, rg_dic = dict(), dict(), dict(), dict()
    for y in range(n):
        for x in range(n):
            tm_ch = char_map_dic[(x,y)]
            if tm_ch == 'R':
                r_dic[(x,y)] = get_adj(char_map_dic, x, y, tm_ch)
                rg_dic[(x,y)] = get_adj(color_blindness_dic, x, y, tm_ch)
            elif tm_ch == 'G':
                g_dic[(x,y)] = get_adj(char_map_dic, x, y, tm_ch)
                rg_dic[(x,y)] = get_adj(color_blindness_dic, x, y, 'R')
            else:
                b_dic[(x,y)] = get_adj(char_map_dic, x, y, tm_ch)
    
    print(len(dfs(r_dic)) + len(dfs(g_dic)) + len(dfs(b_dic)), end=' ')
    print(len(dfs(rg_dic)) + len(dfs(b_dic)), end=' ')

if __name__ == '__main__':
    solution()