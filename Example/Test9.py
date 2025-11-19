#List Slicing
# List[start : stop : step]

a = [10, 20, 30, 40 ,50 ,60]
b = a[2 : 5 : 2]
print(b)
c = a[2 : ]
print(c)
d = a[ : ]
print(d) 

b = a[:: -1] #Lật ngược list
print(b)

a[2 : 5] = [100]
print(a)

a[:0] = [1, 2, 3] #chèn vào đầu list
print(a)
a[len(a):] = [4, 5, 6] #chèn vào cuối list
print(a)

b = a[:]
print(b)
print(a == b)
print(a is b)