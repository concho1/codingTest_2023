import sys
if __name__ == '__main__':
    n = int(input())
    kbs_dic = dict({'KBS1': 0, 'KBS2':0})
    for i in range(n):
        channel = sys.stdin.readline().strip()
        if channel in kbs_dic:
            kbs_dic[channel] = i
    
    # 첫번째 채널을 min(kbs)뒤로 보내버린다.
    min_kbs, max_kbs = min(kbs_dic.values()), max(kbs_dic.values())
    for i in range(min_kbs):
        sys.stdout.write('3')
    # max(kbs)로 커서를 움직인다.
    for i in range(max_kbs- min_kbs):
        sys.stdout.write('1')
    # max(kbs)를 첫번째로 옮긴다.
    for i in range(max_kbs):
        sys.stdout.write('4')
    
    # max(kbs)가 KBS1이면 min_kbs-1, 아니면 min_kbs
    move = min_kbs-1 if max(kbs_dic, key=kbs_dic.get) == 'KBS1' else min_kbs
    for i in range(move): # min(kbs)로 커서를 움직인다.
        sys.stdout.write('1')
    for i in range(move): # min(kbs)를 첫번째 혹은 두번째 위치로 옮긴다.
        sys.stdout.write('3')


    