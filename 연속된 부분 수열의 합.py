def solution(sequence, k):
    answer_dic = dict()
    sum_result, start_index,end_index,answer_flag = sequence[0],0,0,False
    while start_index < len(sequence):
        if sum_result < k:
            end_index += 1
            if end_index >= len(sequence): break
            sum_result += sequence[end_index]
            print(start_index, end_index, sum_result)
        elif sum_result > k or answer_flag == True:
            answer_flag = False
            sum_result -= sequence[start_index]
            start_index += 1
            print(start_index, end_index, sum_result)
        else:
            if not end_index - start_index in answer_dic:
                answer_dic[end_index - start_index] = [start_index, end_index]
            answer_flag = True
            print(start_index, end_index, sum_result)
        
    print(answer_dic)
    print(answer_dic[min(answer_dic)])
    return answer_dic[min(answer_dic)]

sequence = [2, 2, 2, 2, 2]
k = 6

solution(sequence, k)