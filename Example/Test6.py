def sum(a, b):
    return a + b
print(sum(10, 20))
print(sum(3.14, 2.86))
print(sum("Hello ", "Python"))
a = [1, 2, 3]
b = [4, 5, 6]
print(sum(a, b))
print(a + b)
print(a)
print('\n')

def product(a, b):
    a = a* b
    return a
a = 10
b = 20
print(product(a, b))   
print(a)
print('\n')

def XinChao(name1, name2, name3):
    print("Xin chào", name1, name2, name3)
def infor(name, age = 18):
    print("Tên: ", name, end=', ')
    print("Tuổi: ", age)

if __name__ == "__main__":
    print("Chương trình chính")
    print("Tổng 2 số là: ", sum(10, 20))
    print("Tích 2 số là: ", product(10, 20))
    XinChao("An", "Bình", "Cường") #Positional Argument
    XinChao(name3="Cường", name1="An", name2="Bình") #Keyword Argument
    infor("An") #Default Argument
    infor("Bình", 20)
print('\n')