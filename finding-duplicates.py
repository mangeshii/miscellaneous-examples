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
        unique[x] += 1            

           
print(dups)
