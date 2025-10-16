if __name__ == '__main__':
    name = []
    score = []
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
    m = min(score)
    m2 = 1e9
    for i in score:
        if i != m and i < m2:
            m2 = i
    res = []
    for i in range(len(name)):
        if score[i] == m2:
            res.append(name[i])
    res.sort()
    for i in res:
        print(i)