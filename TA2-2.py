q=input()

q_sp= q.split()

a=""

i=0

while i < len(q_sp):
  a +=str(int(q_sp[i])+1)+' '
  
  i +=1

print(a.strip())