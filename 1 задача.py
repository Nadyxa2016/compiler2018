import random

def ex(s, mas, lr):
    if lr!='E':
        d=[]
        i=0
        while (d==[]) & (i<len(mas)):
        # for i in range(len(a)):
            if mas[i][0]==lr :
                d=mas[i][1]
                h=random.choice(d)
                print("h="+str(h))
                for j in h:
                    k=j.lower()
                    if j==k:
                        s+=j
                    else:
                        s=ex(s,mas,j)
            i+=1
    return (s)

f = open('1_zad.txt', 'r')
a=[]
for line  in f:
    b=[]
    if ('\n' in line):
        line=line[:len(line)-1]
    b=line.split('->')
    b[0] = b[0].strip(' ')
    b[1]=b[1].strip(' ')
    c=[]
    c=b[1].split('|')
    e=[]
    e.append(b[0])
    e.append(c)
    a.append(e)

print(a)
s=""
lr="S"
s=ex(s,a,lr)
# print(random.choice(a[1][1]))
print(s)