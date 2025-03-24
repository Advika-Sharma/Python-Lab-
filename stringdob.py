dob={"mothi":"12-11-1990","sudheer":"17-08-1991","vinay":"31-08-1988"} 
str1=input("which person dob you want: ") 
l=str1.split() 
birth="" 
for i in l: 
    if i in dob.keys(): 
        name=i 
print (" ".join([name,"Birthday is",dob[name]])) 
