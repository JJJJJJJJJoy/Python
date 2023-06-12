q=input()

z=q.split()

i=0
a=[]
while i<len(z):
  a.append(z[i][::-1])
  i +=1

print(' '.join(a))