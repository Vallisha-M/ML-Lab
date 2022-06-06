try:
    n=int(input('Enter no. of columns(incl. the last one) : '))
except:
    print("Number of columns should be an integer")
    exit()
assert n>0, "Number of columns should be greater than zero"
print('Enter -1 to stop, last column should be +/-')
x=''
l=[]
while x!='-1':
    x=input('Enter row separated by commas(no space) : ')
    if(x=='-1'):
        break
    x=x.split(',')
    assert len(x)==n, "Check number of columns"
    assert x[-1]=='+'or x[-1]=='-', "Last column should be +/-"
    l.append(x)

hypothesis=['phi' for _ in range(n-1)]
for row in l:
    if row[-1]=='+':
        for j in range(n-1):
            if hypothesis[j]=='phi':
                hypothesis[j]=row[j]
            elif hypothesis[j]!=row[j]:
                hypothesis[j]='?'
print("Most specific hypothesis : ",hypothesis)
