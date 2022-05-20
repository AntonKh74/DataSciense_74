'''Игра компьютер угадает число меньше чем за 20 попыток'''
import numpy as np
    
def random_predict (number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
       int: число попыток угадать число
    """
    
    #вводим ограничения минимум и максимум для интервала выбора числа
    minimum = 1 
    maximum = 101
    count = 0 #вводим переменную, равную 0, для учета числа попыток угадывания
    number = np.random.randint(minimum, maximum) #выбираем рандомное число из заданного интервала
        
    while True: #цикл, в рамках которого алгоритм угадывает число
        count+=1
        #сокращаем число цифр, среди которых ищем искомое число number
        medium = (minimum+maximum) // 2
        if medium > number:
             maximum = medium
             
        elif medium < number:
             minimum = medium
        
        else:
            #print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
    return(count)   
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(20)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

#RUN
score_game(random_predict)