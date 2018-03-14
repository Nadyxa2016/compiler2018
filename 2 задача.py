f = open('2_zad.txt', 'r')
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

f1=True# КС ГРАМ
f2=True# КЗ ЕРАМ
f3=True# А ГРАМ
f=True# ФОРМ ГРАМ

for b in a:
    if b[0].lower()!=b[0]:
        if (len(b[0])!=1) & ((f1==True)|(f3==True)|(f2==True)):
            f1=False
            f3=False
            if 'E' in b[1]:# если правило содержит Е
                    f2=False
            for c in b[1]:
                if len(b[0])<=len(c):
                    n=b[0]
                    m=c
                    t=''
                    while t=='':
                        if n[0]==m[0]:
                            n=n[1:]
                            m=m[1:]
                        else:
                            t=n[0]
                    if len(n)>0:
                        p=''
                        while p=='':
                            if n[len(n)-1]==m[len(m)-1]:
                                n=n[:len(n)-1]
                                m=m[:len(m)-1]
                            else:
                                p=n[len(n)-1]
                        if not((len(n)==1) & (len(m)>0) & (n.lower()!=n)):
                            f2=False
                else:
                    f2=False
        elif (len(b[0])==1) & (f3==True):
            for c in b[1]:
                k=0
                for w in c:
                    w1=w.lower()
                    if w!=w1:
                        k+=1
                if k>1:
                    f3=False
    else:
        f=False

if f:
    if f3:
        print("это А грамматика")
    elif f1:
        print("это КС грамматика")
    elif f2:
        print("это КЗ грамматика")
    else:
        print("это неограниченная грамматика")
else:
    print("это не формальная грамматика")