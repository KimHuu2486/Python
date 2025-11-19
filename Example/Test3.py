if 10 < 20:
    print('10 < 20')
    print('điều kiện đúng')
else :
    print('10 >= 20')
    print('điều kiện sai')

n = 40
if (n < 50) and (n % 2 == 0):
    print(n, "nhỏ hơn 50")
elif (n >= 50) and (n < 100):
    print(n, "lớn hơn hoặc bằng 50 và nhỏ hơn 100")
else:
    print(n, "lớn hơn hoặc bằng 100")
print('\n')

a, b = 10, 20
max = a if a > b else b
print("max =", max)