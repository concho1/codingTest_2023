def solution(name, yearning, photo):
    n_y = dict(zip(name, yearning))
    sol = []
    for p in photo:
        scor = 0
        for p_name in p:
            try:
                print(p_name)
                scor += n_y[p_name]
            except:
                pass
        sol.append(scor)
    return sol


n = ["may", "kein", "kain", "radi"]
y = [5, 10, 1, 3]
p = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

solution(n,y,p)