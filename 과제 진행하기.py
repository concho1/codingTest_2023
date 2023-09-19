def solution(plans):
    answer, overdue_work = [], []
    plans_dic = {0:[0,0]}
    start_time, progress_work = 1441, 0

    for name, start, playtime in plans:
        hour, minute = start.split(':')
        print(int(hour)*60 + int(minute))
        time_minute = int(hour)*60 + int(minute)
        if start_time > time_minute:
            start_time = time_minute
        plans_dic[time_minute] = [name , int(playtime)]
    print(plans_dic)
    for t in range(start_time, 1441):
        # 일이 끝났으면
        if plans_dic[progress_work][1] == 1:
            #끝난일 저장 후
            answer.append(plans_dic[progress_work][0])
            # 밀린 일 있으면 하고 아님 초기화
            if overdue_work:
                progress_work = overdue_work.pop()
            else:
                progress_work = 0
        # t에 시작하기로 한 일이 있는데
        if t in plans_dic:
            # 기존 일이 있으면
            if progress_work != 0:
                # 잠시 저장 후 다른일 시작
                overdue_work.append(progress_work)
                progress_work = t
            #없으면
            else:
                # 바로 다른일 시작
                progress_work = t

        # 일하는 중..
        plans_dic[progress_work][1] -= 1
    print(answer)
    print(plans_dic)
    return answer

plans = [["korean", "11:40", "30"], ["english", "11:10", "20"], ["math", "12:30", "40"]]
solution(plans)