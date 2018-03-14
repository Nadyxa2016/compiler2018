import re

def rdel_sk(rg):
    i=[]
    f=[]
    sk=0
    rg=rg+' '
    for j in range(len(rg)):
        if rg[j] == '(':
            w = [j, 0]
            f.append(w)
            sk += 1
        elif rg[j] == ')':
            sk -= 1
            k=len(f)
            while k>0:
                k-=1
                if f[k][1]==0:
                    f[k][1] = j
                    k=-1

        elif rg[j]=='E':
            i.append(j)
    for h in i:# для каждой Е
        s=len(rg)
        k=h
        for j in range(len(f)):#находим в какой она скобке
            if (h>f[j][0]) & (h<f[j][1]):
                if (f[j][1]-f[j][0]<s):
                    k = f[j][1]
                    s = f[j][1] - f[j][0]
        if (rg[k+1]!='*'):
            rg=rg[:k+1]+'?'+rg[k+2:]
            for p in i:
                if p>k+1:
                    p+=1
            for p in f:
                if p[0]>k+1:
                    p[0]+=1
                if p[1]>k+1:
                    p[1]+=1
    return rg

def rdel_or(rg):
    m=[]
    sk=0
    r=rg+'+'
    i=0
    while i<(len(r)):
        if ((r[i]=='+') | (r[i]=='|')) & (sk==0):
            m.append(r[:i])
            r=r[i+1:]
            i=0
        elif r[i]=='(':
            sk+=1
            i += 1
        elif r[i]==')':
            sk-=1
            i += 1
        else:
            i+=1
    return m

f=open('6_zad.txt','r')
st=f.readline()
rg=f.readline()
if '\n' in st:
    st=st[:len(st)-1]
if '\n' in rg:
    rg=rg[:len(rg)-1]
print(st,rg)
for i in range(len(rg)):
    if rg[i]=='+':
        rg=rg[:i]+'|'+rg[i+1:]
rg=rdel_sk(rg)
rg=rg[:len(rg)-1]
mas=rdel_or(rg)
rg=''
for a in mas:
    rg+='^'+a+'$|'
rg=rg[:len(rg)-1]
if re.match(rg,st) is not None:
    print(True)
else:
    print(False)