arr = [1,2, 2.5, "Kim Huu"]
print(arr)
print(type(arr))

s = "Kim Huu"
a = list(s)
print(a)

print(list(range(20)))
print(len(a))

print(a[0])
print(a[-1]) #Chỉ số âm
#print(a[10]) Error
print("\n")

for i in range (len(a)):
    print(a[i], end = " ")
print("\n")
for i in a:
    print(i, end = " ")
print("\n")

arr.append("Tran")
print(arr)
arr.insert(2, 3)
print(arr)

arr.pop()
print(arr)
arr.pop(1) #Xóa tại index 1
print(arr)
del arr[0] #xóa tại index 0
print(arr)
print("\n")

a = [1, 2, 1, 2, 3, 2]
print(a)
a.remove(2) #xóa value 2 đầu tiên
print(a)
a.clear()
print(a)
print("\n")

a = [1, 2, 3]
b = a * 2
print(b)
print([0] * 10)
print("\n")

a = [1, 2, 3, 4, 5]
if 3 in a:
    print("YES")
print("\n")

a = [1, 2, 3]
b = [4, 5, 6]
a+=b
print(a)
a.extend(b)
print(a)
print("\n")

a = [1, 2, 3]
b = a
c = a.copy()
print(a is b)
print(c)
print(c is a)
print(c == a)
print("\n")

a = [1, 2, 1, 2, 3]
print(a.count(1))
print(a.index(2))

a.reverse()
print(a)
a.sort()
print(a)
print(max(a))
print(min(a))
print(sum(a))

a = [5, 2, 3, 4]
b = sorted(a)
print(a)
print(b)