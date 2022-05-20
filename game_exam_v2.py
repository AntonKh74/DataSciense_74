"""Игра Угадай число: компьютер сам загадывает число, а после сам его угадывает"""

import numpy as np #импортировали нужную библиотеку

def random_predict (number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
       int: число попыток угадать число
    """
    count = 0 #число попыток угадать, по умолчанию присваиваем 0
    
    while True: 
        count += 1 #увеличиваем число попыток
        predict_number = np.random.randint(1,101) #присваиваем переменной случайное значение от 1 до 100
        if number == predict_number: #проверяем, равно ли значение загаданного числа присвоенному выше
            break #если угадали, прерываем цикл
        
    return (count)

def score_game (random_predict)->int:
    """Подсчет попыток, за сколько в среднем угадывается число из 1000 попыток

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: число, за которое в среднем угадывается число
    """
    count_ls = [] #пустоя список для хранения числа попыток до угадывания в каждой итерации
    np.random.seed(1) #фиксируем сид для воспроизводимости 
    random_array = np.random.randint(1, 101, size=(1000)) #загадан список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return(score)
       
# RUN  
score_game (random_predict)