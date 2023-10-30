d,m,y=map(int,input().split())
b=y%100
c=y//100
w=d+int((13*(m+1))/5)+b+int(b/4)+int(c/4)+5*c
w=w%7
print(w)
if m==1:
    w+=2
elif m==2:
    w+=3
if w==0 or w==7:
    print("saturday")
elif w==1 or w==8: 
    print("Sunday")
elif w==2:
    print("Monday")
elif w==3:
    print("Tuesday")
elif w==4:
    print("Wednesday")
elif w==5:
    print("Thursday")
elif w==6:
    print("Friday")
