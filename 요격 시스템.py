def solution(targets):
    answer = 0
    targets.sort(key=lambda x : x[1])
    length = len(targets)
    i = 0
    tm_i = 1
    cnt = 1
    while tm_i < length:
        if targets[i][1] <= targets[tm_i][0]:
            i = tm_i
            cnt += 1
        tm_i += 1
        print(cnt)
    print(targets)
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
solution(targets)