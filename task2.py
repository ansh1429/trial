inp= int(input("enter no of students : "));
eng=0
maths=0
sci=0
d1=dict()

li=[]
for i in range(0,inp):
    name=input("enter name  :")
    eng=int(input("enter marks in english : "))
    if(eng>100):
        flag=0
        while flag==0:
            eng = int(input("enter marks less than 100 : "))
            if(eng<=100):
                flag=1
                
    maths=int(input("enter marks in maths : "))
    if(maths>100):
        flag=0
        while flag==0:
            maths = int(input("enter marks less than 100 : "))
            if(eng<=100):
                flag=1
                
    sci=int(input("enter marks in science : "))
    if(sci>100):
        flag=0
        while flag==0:
            sci = int(input("enter marks less than 100 : "))
            if(eng<=100):
                flag=1
               
    d1={
   "name":name,
   "eng":eng,
   "maths":maths,
   "sci":sci
        }
    li.append(d1)


    
print(li)


m1={}
li2=[]
for i in li:
    
    if(i['eng']>=i['maths'] and i['eng']>=i['sci']):
        h = "english"
        if(i['eng']==i['maths']):
            h+= " and maths" 
        elif(i['eng']==i['sci']):
            h+= " and science" 
    elif(i['maths']>=i['eng'] and i['maths']>=i['sci']):
        h = "maths" 
        if(i['maths']==i['sci']):
            h+= " and science" 
    else:
        h = 'sci = ',i['sci']
    
    
    
    s= i['eng']+i['maths']+i['sci']
    percent = round(s/3)
    m1={
        "name":i['name'],
        "highest" : h,
        "total":s,
        "percentage":percent
        
        }
    li2.append(m1)

print(li2)


flag=True;
while flag:
    re=input("Result of any other student yes/no? ").casefold()
    if(re=='yes'):
        n1=input("enter name : ")
        f=0
        for i in li:
            if(i['name'].casefold()==n1.casefold()):
                print(i)
                f+=1
        if(f==0):
            print("No student found")
    elif(re=='no'):
        print("okay, visit again !!")
        flag=False
    else:
        print("enter only yes or no")
    






























    