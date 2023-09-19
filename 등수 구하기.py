# 10 <= P <= 50, 0 <= N <= P, 0 <= score <= 2000000000
# 1) N>0 일때만 입력받는다, N == 0 일땐 무조건 1등
# 2) 입력에 tasu의 점수를 추가해 sc_list를 정렬한다.
# 3) P==N 이고 마지막 점수가 태수의 점수이면 순위를 벗어난것과 동일
# 4) tasu 점수의 index+1이 등수
if __name__ == '__main__':
    N, tasu, P = map(int, input().split())
    if N > 0:
        sc_l = sorted(list(map(int, (input()+' '+str(tasu)).split())), reverse=True)
        print('-1' if tasu == sc_l[N] and P == N else sc_l.index(tasu)+1)
    else:
        print('1')