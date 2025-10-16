print("hello world!!!")
print('hello world!!!')
print(1 + 3)
print("cplusplus", "python", "java", sep="#", end ="----->")
print("cplusplus", "python", "java", sep="#")
#chú thích
#thêm một dòng nữa
"""
chú thích nhiều dòng
print("hello world!!!")
"""
a = 100
s = "kim huu"
print(type(a))
print(type(s))
b = 3.14
print(type(b))
c = True
print(type(c))
print(a, s, b, c, sep = "---")
d = 3 + 4j
print(type(d))
print(d)

a = 0b1001  #hệ nhị phân
print(a)
b = 0o11   #hệ bát phân
print(b)
c = 0x1A   #hệ thập lục phân
print(c)

print('\n')
a = 3.5
b = 3e5
d = 1.9e308
e = 5.4e-325
print(a)
print(b)
print(d)
print(e)
print('\n')

a = 28.04234323
print(round(a, 3))
print('%.2f' % a)
print(format(a, '.4f'))
print('{:.3f}'.format(a))
print('\n')

s = "Hello Python"
print(type(s))
s = '''Hello
Python'''
print(s)
print(type(s))
print(s[0])
s = '123456789'
a = int(s)
print(a)
print(type(a))
print('\n')

a = str(100)
b = str(3.14)
c = str(True)
print(a, b, c)

a, b, c = 10, 3.14, "Hello"
print(a, b, c)

a, b = b, a
print(a, b, '\n')

a = 10
b = 3
mod = a //b #chia lấy phần nguyên
print(mod)
re = a % b  #chia lấy phần dư
print(re)
print(a**b) #lũy thừa
print('\n')


a = True
b = False
print(a and b)
print(a or b)
print(not a)
print('\n')

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a is not b)
print(a == b)
print(a != b)
print('\n')

s = 'Hello Python'
print('H' in s)
print('Python' in s)
print('Java' not in s)
print('\n')

"""n = int(input("Nhập n: "))
if n % 2 == 0:
    print(n, "là số chẵn")
else:
    print(n, "là số lẻ")
s = input("Nhập chuỗi: ")
print("Chuỗi vừa nhập là: ", s)
print('\n')"""

s = input("nhập 3 số: ")
a = s.split()
print(a)
x, y, z = map(int, a)
print("3 số vừa nhập là: ", x, y, z)
print(x + y + z)
print('\n')

x, y, z, t = map(int, input("Nhập 4 số: ").split())
print(x, y, z, t)