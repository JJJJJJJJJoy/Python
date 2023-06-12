a=input()
b=a.split()
x = int(b[0])
y = int(b[1])
i=1 

while i <= x:
  k=1
  
  while k <= y :
    print(f'{i}x{k}={i*k}')
    k +=1
  i +=1
