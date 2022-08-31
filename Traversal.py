# Linear Traversal
#Use case- Finding maximum value in an array l
#Time complexity- O(n) and auxiliary space- O(1) as one extra variable v was created 
v = l[0]
for i in range(1,len(l)):
  if l[i] > v:
    v = l[i]
print(v)
