a='abcduebak'
lst=list(a)


unique={}
dups=[]

for x in lst:
    if x not in unique:
        unique[x]=1
    else:
        if unique[x] == 1:
            dups.append(x)
        unique[x]+=1         

print(dups)


###################################################


a='abcduebak'
lst=list(a)

dups=[]
for i in lst:
    if i not in dups:
        dups.append(i)
    else:
        print('{}'.format(i), end=" ")
