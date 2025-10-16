n = 0
while (n<=5):
    print(n, end=' ')
    n+=1
else:
    print("Hết vòng lặp, giá trị n = ", n)
print('\n')

n = 123456
cnt = 0
while (n!=0):
    n//=10
    cnt+=1
print("Số chữ số là: ", cnt)

n  = 1234
sum = 0
while (n!=0):
    sum += n % 10
    n//=10
print("Tổng các chữ số là: ", sum)