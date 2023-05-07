from sys import argv


f = open(argv[1], 'r')
f1 = open(argv[2], 'w+')
linecnt = 0

while True:
    linecnt += 1  
    line = f.readline()
    if not line:
        break
    llist = line.split()
    
    try:
        if llist[2] == 'gene':
            print(f'chr{llist[0]}\t{llist[3]}\t{llist[4]}\t{llist[6]}\t{llist[15][1:-2]}\t{llist[11][1:-2]}\t{int(llist[4])-int(llist[3])}', file=f1)
    except:
        continue
f.close()
f1.close()