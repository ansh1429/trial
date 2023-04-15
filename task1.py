
'''
a=[1,7,2,7,3,7,8,7]
def repeat(x):
    size = len(a);
    rep=[];
    for i in range(0,size):
        k=i+1;
        for j in range(k,size):
            if(x[i]==x[j] not in rep):
                rep.append(x[i])
                
                
    return rep

z=repeat(a)
print(z)

ind=[]
for i in range(0,len(a)):
    if a[i]==z[0]:
        ind.append(i);
n1=ind[0]
n2=ind[-1]
list1=[n1,n2]
print(list1)


sum=0
li=[7,8,5,4,10]
inp=15;



for i in li:
    new=[]
    for j in li:
        if(i!=j):
            if(inp==i+j):
                new.append(i)
                new.append(j)
                outer.append(new)
             
print(outer)

for i in outer:
    for j in i:
        for k in i:
            if(k==j):
    
                
   
         
print(outer)
    
  '''
  
  
li=[7,8,5,4,10]
inp=15;
new=[]
outer=[]


for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        if(inp==li[i]+li[j]):  
            new.append(li[i])
            new.append(li[j])
            outer.append(new)
print(outer)
    




  
  
  
  
  
  
  
  
  
  
  
           
                
            

    