#1 вар.
while True:
    a = input("Задайте диапазон данных массива от: ")
    b = input("Задайте диапазон данных массива до: ")
    c = int(a)
    d = int(b)
    print([x for x in range(c,d)if x%3==0])

#2 вар.
while True:
    a = input("Задайте диапазон данных массива от: ")
    b = input("Задайте диапазон данных массива до: ")
    c = int(a)
    d = int(b)
    x = list(range(c,d))
    for i in x:
        if i%3==0:
            print(i)
