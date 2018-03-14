import random

def ex(mas, s, word):
    if (s.lower()==s) & (s==word):
        return True
    elif (len(s)<=len(word)):
        for i in range(len(s)):
            if s[i].upper()==s[i]:
                d = []
                j=0
                while (d == []) & (j < len(mas)):
                    if mas[j][0] == s[i]:
                        d=mas[j][1]
                        for k in d:
                            s1=s[:i]+str(k)+s[i+1:len(s)]
                            fv=False
                            kol=0
                            ind=0
                            for v in range(len(s1)):
                                if s1[v]=='E':
                                    fv=True
                                    ind=v
                                if s1[v]==s1[v].upper():
                                    kol+=1
                            if (kol==1) & fv:
                                s1=s[:ind]+s[ind+1:len(s)]

                            if (len(s1) <= len(word)):
                                #print(s1)
                                f1=ex(mas, s1, word)
                                if f1:
                                    return True
                    j+=1
    else:
        return False



f = open('5_zad.txt', 'r')
word=f.readline()
if '\n' in word:
    word=word[:len(word)-1]
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

print(word)
print(a)
f=False
s="S"
f=ex(a,s,word)
print(f)