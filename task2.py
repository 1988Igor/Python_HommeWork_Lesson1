#Напишите программу, которая принимает на вход координаты 
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

coordinates_x =int(input('Enter the coordinates for \"x"'))
coordinates_y =int(input('Enter the coordinates for \"y"'))
if (coordinates_x==0 and coordinates_y==0):
    print('Please introduce the coordinate biger than \"0" ')
elif(coordinates_x>0 and coordinates_y>0):
    print('quarter 1')
elif(coordinates_x<0 and coordinates_y>0):
    print('quarter 2')
elif(coordinates_x<0 and coordinates_y<0):
    print('quarter 3')
elif(coordinates_x>0 and coordinates_y<0):
    print('quarter 4')