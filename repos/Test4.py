#range(start, stop, step)
#start: giá trị bắt đầu (mặc định là 0)
#stop: giá trị kết thúc (không bao gồm giá trị này)
#step: bước nhảy (mặc định là 1)
a = range(1, 10, 2)
for i in a:
    print(i, end=' ')
print('\n')

for i in range(51):
    print(i, end=' ')
print('\n')

for i in range(10, 0, -1):
    print(i, end=' ')
else :
    print("Hết vòng lặp")
print('\n')

for i in range(1, 7):
    print(i, end = ' ')
    i+=1000
    print(i)
print('\n')

for i in range(1, 21):
    if i % 7 == 0:
        break
    print(i, end = ' ')
    print('Câu lệnh dưới break')
print('\n')

for i in range(3):
    for j in range(2):
        print(i, j)
print('\n')