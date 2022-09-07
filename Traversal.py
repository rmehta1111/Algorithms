# Linear Traversal
#Use case- Finding maximum value in an array l
#Time complexity- O(n) and auxiliary space- O(1) as one extra variable v was created 
v = l[0]
for i in range(1,len(l)):
  if l[i] > v:
    v = l[i]
print(v)

#Code snippet for solving lot of codechef problems where would need to process alternate inputs:
i =int(input())
for j in range(2*i):
    if j%2 == 0:
        f,s = map(int,input().split())
        A=1;
    else:
        nf,ns = map(int,input().split())
        if not (nf < f) and not (ns < s):
            print('POSSIBLE')
        else:
            print ('IMPOSSIBLE')
