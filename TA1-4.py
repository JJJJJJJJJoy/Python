n=input()

b=n.split(',')
q=b[0].split()
a=b[1].split()

c=0

if q[0] in a:
  c +=1
if q[1] in a:
  c +=1
if q[2] in a:
  c +=1
if q[3] in a:
  c +=1
if q[4] in a:
  c +=1
  
if c<3:
  print(0)
elif c==3:
  print(100)
elif c==4:
  print(1000)
else:
  print(10000)