"""Игра Угадай число: компьютер сам загадывает число, а после сам его угадывает"""

from itertools import count
import numpy as np #импортировали нужную для работы библиотеку

number = np.random.randint(1, 101) #загадываем число и записываем его в переменнюу number ,
# само число выбирается рандомайзером в отрезке от 1 до 100 (101 пишем так, как отсчет идет ДО и не включает 101)

print (number)

count = 0 # в переменную будем записывать число попыток и изначально приравниваем ее к 0

while True: #цикл, который пытается угадывать число
    count += 1 #увеличиваем переменную с числом попыток
    predict_number = int(input("Введите число от 1 до 100")) #вводим переменную, в которую записываем то число, которое ввел игрок
    
    if predict_number > number: #проверяем, больше ли введенное число, чем загаданное машиной
        print ("Ваше число больше того, что я загадал")
        
    elif predict_number < number: #проверяем, меньше ли введенное число, чем загаданное машиной
        print ("Ваше число меньше того, что я загадал")
        
    else:
        print (f"Вы угадали число. Это {number}, вам на это понадобилось {count} попыток")
        break
    
    