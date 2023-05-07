from sys import argv

def prt(m):
    if len(m) == 0 or m[1][-4:-1] != 'AGA':
        return
    print(m[0][:-1])
    print(m[1][:-2] + 'CT')
    if m[2][0] == '+':
        print('+')
        print(m[3][:-2] + m[3][-4:-2])
    else:
        print(m[2][:-2] + m[2][-4:-2])

f = open(argv[1], 'r')
m = []

for line in f:
    if line[0] == '@':
        if len(m) > 0:
            prt(m)
        m = []       
    m.append(line)
prt(m)

f.close()

