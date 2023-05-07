import re
from sys import argv


f = open(argv[1], 'r')
f1 = open(argv[2], 'w')
linecnt = 0

c1 = re.compile('\d+M')
c2 = re.compile('(\d+)M(\d+)N(\d+)M')
cnt1 = 0
cnt2 = 0

while True:
    linecnt += 1
    line = f.readline().strip()
    if not line:
        break
    llist = line.split()
    tline = llist[6]
    
    if len(c1.findall(tline)) == 1:
        cnt1 += 1
        print(line, file=f1)
    elif len(c1.findall(tline)) == 2:        
        l2 = c2.findall(tline)
        if len(l2)>0:
            cnt2 += 1
            if int(l2[0][0]) > int(l2[0][2]):
                tmp = int(llist[1]) + int(l2[0][0])
                llist[2] = str(tmp)
                print('\t'.join(llist), file=f1)
            else:
                tmp = int(llist[2]) - int(l2[0][2])
                llist[1] = str(tmp)
                print('\t'.join(llist), file=f1)
f.close()
print(f'full match {cnt1}')
print(f'central gap {cnt2}')

