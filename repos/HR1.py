n = int(input())
if n % 2 == 1:
    print("WEIRD")
else:
    if (n in range(2, 5)):
        print("NOT WEIRD")
    elif (n in range(6, 20)):
        print("WEIRD")
    else:
        print("NOT WEIRD")