t=int(input())
for i in range (0,t):
    x=input()
    y=0
    z=0
    if(len(x)==10):
        y+=1 
    if(len(set(x))==len(x)):
        y+=1 
    if x.isalnum(): 
        y+=1 
    for char in x:
        if char.isdigit():
            z+=1
    if(z>=3):
        y+=1
    z=0
    for char in x:
        if char.isupper():
            z+=1
    if(z>=2):
        y+=1
    
    if(y>=5):
        print("Valid")
    else:
        print("Invalid")