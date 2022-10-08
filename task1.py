#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
number_day = int(input('Enter a number of day'))
if(number_day <= 5):
    print('No, this day is not Weekend')
elif(number_day <= 7):
    print('Yes, this day is Weekend')
else:
    print("Please choose an another number of day of the Week:")

