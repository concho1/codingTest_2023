# 풀이 설계
# 풀기 편하게 리스트 형식으로 만들어 준다.
# . 개수를 cnt한다, x 면 초기화
# . 개수가 2개이면 누울수 있는 자리로 cnt
# 방을 회전시킨다.
# 위 과정을 다시 한다.
# 끝
import sys
def dot_cal(str_list):
    total_cnt = 0
    for st in str_list:
        dot_cnt = 0
        for ch in st:
            if ch == '.':
                dot_cnt += 1
            else:
                dot_cnt = 0

            if dot_cnt == 2:
                total_cnt += 1
    return total_cnt
    
def turn_list(str_list,n):
    new_list = []
    for i in range(n):
        tm_list = []
        for j in range(n):
            tm_list.append(str_list[j][i])
        new_list.append(''.join(tm_list))
    return new_list

if __name__ == '__main__':
    n = int(input())
    str_list = []
    for _ in range(n):
        str_list.append(sys.stdin.readline().replace('\n',''))

    print(dot_cal(str_list), end=' ')
    print(dot_cal(turn_list(str_list, n)))