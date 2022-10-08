#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#coordinates_x =int(input('Enter the coordinates for \"x"'))
#coordinates_y =int(input('Enter the coordinates for \"y"'))
quarter =int(input('"Enter a number of quarter (1 to 4) "'))
if (quarter== 0):
    print('Please introduce the coordinate biger than \"0" ')
elif(quarter==1):
    print(f'The range of possible coordinates of points in quarter {quarter} are \" x>0 and y>0 " ')
elif(quarter==2):
    print(f'The range of possible coordinates of points in quarter {quarter} are \" x<0 and y>0 " ')
elif(quarter==3):
    print(f'The range of possible coordinates of points in quarter {quarter} are \" x<0 and y<0 " ')
elif(quarter==4):
    print(f'The range of possible coordinates of points in quarter {quarter} are \" x>0 and y<0 " ')