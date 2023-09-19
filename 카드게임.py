# 풀이 설계
# 일단 규칙대로 처리하는 함수 하나 만든다.

def cal_score(c, ns):
    score = []
    # 조건1 & 4
    if len(set(c)) == 1:
        sort_n = sorted(ns)
        tm = sort_n[0]
        for s_n in sort_n[1:5]:
            tm += 1
            if tm != s_n:
                tm = -100
        if tm > 0:
            score.append(sort_n[4] + 900)
        score.append(sort_n[4] + 600)
    # 조건 5
    if True:
        sort_n = sorted(ns)
        tm = sort_n[0]
        for s_n in sort_n[1:5]:
            tm += 1
            if tm != s_n:
                tm = -100
        if tm > 0:
            score.append(sort_n[4] + 500)

    # 조건 6
    if True:
        ns_set = set(ns)
        same_card_cnt = dict()
        for ns_pop in ns_set:
            same_card_cnt[ns_pop] = 0
        for n in ns:
            same_card_cnt[n] += 1
        if 3 in same_card_cnt.values():
            for n in same_card_cnt:
                if same_card_cnt[n] == 3:
                    score.append(n + 400)
                    
    # 조건2 & 3
    if len(set(ns)) == 2:
        ns_set = set(ns)
        same_card_cnt = {ns_set.pop():0, ns_set.pop():0}
        for n in ns:
            same_card_cnt[n] += 1
        if 3 in same_card_cnt.values():
            tm_score = 0
            for n in same_card_cnt:
                if same_card_cnt[n] == 3:
                    tm_score += n * 10
                else:
                    tm_score += n
            score.append(tm_score + 700)
            
        elif 4 in same_card_cnt.values():
            tm_score = 0
            for n in same_card_cnt:
                if same_card_cnt[n] == 4:
                    tm_score = n +800
            score.append(tm_score)

        #print(same_card_cnt)

    # 조건 7 & 8
    if True:
        ns_set = set(ns)
        for ns_pop in ns_set:
            same_card_cnt[ns_pop] = 0
        for n in ns:
            same_card_cnt[n] += 1
        two_cnt, two_card = 0, []
        if 2 in same_card_cnt.values():
            for n in same_card_cnt:
                if same_card_cnt[n] == 2:
                    two_cnt += 1
                    two_card.append(n)
            if two_cnt == 2:
                score.append(10 * max(two_card) + min(two_card) + 300)
            elif two_cnt == 1:
                score.append(two_card.pop()+200)
    if not score:
        score.append(max(ns) + 100)

    return max(score)

if __name__ == '__main__':
    color = []
    num = []
    for _ in range(5):
        color_tm, num_tm = input().split(' ')
        color.append(color_tm)
        num.append(int(num_tm))
    #print(color,num)
    sol = cal_score(color,num)
    print(sol)