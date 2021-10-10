/Solved quickly but only passed 8 test cases, redid the problem later and passed 10/10 cases
arr = []
b = []
l = []
r = []
fin = open("buckets.in", "r")
fout = open("buckets.out", "w")
for i in range(10):
    arr.append(fin.readline())
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'B':
            b.append(i)
            b.append(j)
        if arr[i][j] == 'L':
            l.append(i)
            l.append(j)
        if arr[i][j] == 'R':
            r.append(i)
            r.append(j)
xval = abs(l[0] - b[0])
yval = abs(l[1] - b[1])
rxval = abs(r[0] - b[0])
ryval = abs(r[1] - b[1])
if b[0] == l[0] == r[0] or b[1] == l[1] == r[1]:
    if abs(rxval < xval or ryval < yval):
        fout.write(str(xval+yval+1))
    else:
        fout.write(str(xval + yval - 1))
else:
    fout.write(str(xval + yval - 1))
