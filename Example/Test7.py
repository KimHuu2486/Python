def solve():
    n = (int)(input("Nhập n: "))
    if n %3 == 0 and n %5 == 0:
        print("YES")
    else:
        print("NO")

def check(n):
    if n%3 == 0 and n%5 == 0:
        return True
    return False

def tonghieu(a, b):
    tong = a + b
    hieu = a - b 
    return tong, hieu

if __name__ == "__main__":
    n = (int)(input("Nhập n: "))
    if check(n):
        print("YES")
    else:
        print("NO")
    print(tonghieu(10, 5))
