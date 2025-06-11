

i = [i for i in range(1,10,2)]
print(i)
j = [j for j in range(0,10,2)]
print(j)

ip = 0
jp = 0

merged = []
while(ip < len(i) and jp < len(j)):
    if i[ip] < j[jp]:
        merged.append(i[ip])
        ip+=1
    else:
        merged.append(j[jp])
        jp+=1
while ip < len(i):
    merged.append(i[ip])
    ip+=1
while jp < len(j):
    merged.append(j[jp])
    jp+=1
    
print(merged)
