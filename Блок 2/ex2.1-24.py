x = float(input('x = '));
y = float(input('y = '));

#y=-x-1 and x<=0 and y<=0
#x=-1 and y>=0 and y<=-1
#y=-1 and x>=0 and x<=-1

if (y<-x-1) and (x>-1) and (y>-1):
    print("Да");
elif (y<=0 and x<=0 and ((y == -x-1) or (x==-1) or (y==-1))):
    print("На границе");
else:
    print("Нет");
