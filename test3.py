#1 вар.
print([x for x in range(0,10)if x%3==0])

#2 вар.
x = list(range(0,10))
for i in x:
    if i%3==0:
        print(i)
