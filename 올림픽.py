import sys
if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().strip().split(' '))
    con, k_list = [], []
    for _ in range(n):
        tm = list(map(int, sys.stdin.readline().strip().split(' ')))
        if tm[0] == k:
            k_list = tm
        con.append(tm)
    # 금, 은, 동 순으로 정렬
    con.sort(key=lambda x:(-x[1],-x[2],-x[3]))
    rank = con.index(k_list) + 1
    # 내 위에 같은 등수의 국가가 몇개인지 확인
    same_rank_cnt = 0
    for i in range(rank-2, -1, -1):
        if k_list[1:4] == con[i][1:4]:
            same_rank_cnt += 1
        else:
            break
    print(rank-same_rank_cnt)