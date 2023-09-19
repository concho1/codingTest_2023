import sys
# 난쟁이 9명에서 2명을 빼는 경우 => 9C2 => 36
# 조합 구현 귀찮아서 순열로
def solution():
    person_9, person_7_gr, combination_set = [], [], set()
    for _ in range(9):
        person_9.append(int(sys.stdin.readline().rstrip()))
    for i in range(9):
        for j in range(9):
            if i != j:
                tm_person = person_9.copy()
                del tm_person[i]
                del tm_person[j if i > j else j-1]
                person_7_gr.append(tm_person)
    for person_7 in person_7_gr:
        if sum(person_7) == 100:
            person_7.sort()
            for person in person_7:
                print(person)
            break
    
if __name__ == '__main__':
    solution()