from tkinter import E


a = "venkatesh"
b = []   
for i in a:
    if i == "e":
        b += "x"
    else:
        b += i 
print(a)
print(b)

counter=0
for i in b:
    if i == "x":
        b[counter] = "e"
        
   
    counter +=1
print(b)
    
           
           

    
    
