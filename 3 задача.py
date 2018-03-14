f = open('3_zad.txt', 'r')
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

f1=True# ГРЕЙБАХ
f2=True# ХОМСКИЙ
f3=True# ЛЕВО
f4=True# ПРАВО
f=True

for b in a:
    if (b[0].upper()==b[0]) & (len(b[0])==1):
        for c in b[1]:
            if (c.upper()==c) & (c!='E') & (f1|f3|f4) & f:# если только нетерминалы
                f1=f3=f4=False
            elif (c.lower()!=c) & (c!='E') & f:
                f2=False
                if (c[0]!=c[0].lower()):
                    f1=False
                if len(c[1:])>0:
                    if (c[1:]!=c[1:].upper()):
                        f1=False

                k = 0
                for w in c:
                    w1 = w.lower()
                    if w != w1:
                        k += 1
                if k > 1:
                    f3 = f4 = False

                if f4 & (c[0]==c[0].upper()):
                    f3=False
                if f3 & (c[len(c)-1]==c[len(c)-1].upper()):
                    f4=False

            elif f & (c.lower()==c):
                if len(c)>1:
                    f=False


    else:
        f=False

if f:
    if f2:
        print("это нормальная форма Хомского")
    elif f1:
        print("это нормальная форма Грейбах")
    elif f3:
        print("это левая грамматика")
    elif f4:
        print("это правая грамматика")
    else:
        print("это просто кс грамматика")
else:
    print("это не кс грамматика")