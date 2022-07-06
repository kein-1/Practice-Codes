

l = [1,2,3]
n = []
a = len(l)


for i in range(a):
    n.insert(i,l[i])
    n.insert(i+a,l[i])
    print(n)

print(n)