import sys
def solution(n):
    Trans_dic = {
        'A': '1 2\n1 3\n2 3\n',
        '#A': '2 1\n2 3\n1 3\n',
        '@A': '1 3\n1 2\n3 2\n',
        '#@A': '2 3\n2 1\n3 1\n',
        '@#A': '3 1\n3 2\n1 2\n',
        '@#@A': '3 2\n3 1\n2 1\n',
        '#@#A': '3 2\n3 1\n2 1\n',
        'B' : '1 3\n',
        '#B' : '2 3\n',
        '@B' : '1 2\n',
        '@#B' : '3 2\n',
        '#@B' : '2 1\n',
        '@#@B' : '3 1\n',
        '#@#B' : '3 1\n',
    }
    def calculation(cl):
        if "@@" in cl:
            return cl.replace("@@", "")
        elif '##' in cl:
            return cl.replace('##', "")
        elif "#@#@" in cl:
            return cl.replace("#@#@", "@#")
        elif "@#@#" in cl:
            return cl.replace("@#@#", "#@")
        else:
            return cl

    def formula(block):
        new_block = []
        for i in range(len(block)):
            new_block.append( calculation( ''.join(['@',block[i]]) ) )
        new_block.append('B')
        for i in range(len(block)):
            new_block.append( calculation( ''.join(['#',block[i]]) ) )
        
        return new_block
    
    result = []
    block = ['A']
    
    for _ in range(n-2):
        block = formula(block)
    
    for st in block:
        result.extend(Trans_dic.get(st))

    print(len(result)//4)

    return ''.join(result)

n = int(input())

if n == 1:
    sys.stdout.write('1\n1 3')
elif n > 20:
    sys.stdout.write(str(2**n-1))
else:
    sys.stdout.write(solution(n))
