a = {'venki': 100, 'arun': 200, 'anju': 700}
b = []
for key in a:
    
    b.append(a[key])
c =(max(b))
print(c)

for i in a:
    if a[i] == c:
        print(i)
        

