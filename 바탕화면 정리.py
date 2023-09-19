import multiprocessing

def solution(wallpaper):
    answer = []
    
    def sol0(wallpaper):
        col = len(wallpaper)
        row = len(wallpaper[0])
        # 북쪽부터 (#)위치 찾기
        for i in range(col):
            for j in range(row):
                if wallpaper[i][j] == '#':
                    answer.append(i)
                    break
            if wallpaper[i][j] == '#':
                    break
    def sol1(wallpaper):
        col = len(wallpaper)
        row = len(wallpaper[0])    
        # 서쪽부터 (#)위치 찾기
        for j in range(row):
            for i in range(col):
                if wallpaper[i][j] == '#':
                    answer.append(j)
                    break
            if wallpaper[i][j] == '#':
                    break
    def sol2(wallpaper):
        col = len(wallpaper)
        row = len(wallpaper[0])
        # 남쪽부터 (#)위치 찾기
        for i in range(col,-1,-1):
            for j in range(row,-1,-1):
                if wallpaper[i-1][j-1] == '#':
                    answer.append(i)
                    break
            if wallpaper[i-1][j-1] == '#':
                    break
    def sol3(wallpaper):
        col = len(wallpaper)
        row = len(wallpaper[0])    
        # 동쪽부터 (#)위치 찾기
        for j in range(row,-1,-1):
            for i in range(col,-1,-1):
                if wallpaper[i-1][j-1] == '#':
                    answer.append(j)
                    break
            if wallpaper[i-1][j-1] == '#':
                    break
    
    p0 = multiprocessing.Process(target=sol0(wallpaper))
    p1 = multiprocessing.Process(target=sol1(wallpaper))
    p2 = multiprocessing.Process(target=sol2(wallpaper))
    p3 = multiprocessing.Process(target=sol3(wallpaper))
    p0.start()
    p1.start()
    p2.start()
    p3.start()
    return answer