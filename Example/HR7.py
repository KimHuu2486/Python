if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    Max = max(arr)
    res = -1
    for i in arr:
        if i != Max and i > res:
            res = i
    print(res)