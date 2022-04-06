x = input().split(' ')
lst = [[]]
dop = []
for i in range(len(x)):
    for j in range(len(x)):
        dop = x[j:i+j+1]
        if len(dop) == i+1:
            lst.append(dop)
print(lst)