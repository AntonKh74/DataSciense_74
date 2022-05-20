'''Игра компьютер угадает число меньше чем за 20 попыток'''
import numpy as np
    
def random_predict (number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
       int: число попыток угадать число
    """
    minimum = 1
    maximum = 101
    count = 0
    number = np.random.randint(minimum, maximum)
        
    while True:
        count+=1
        medium = round((minimum+maximum) / 2)
        if medium > number:
             maximum = medium
             
        elif medium < number:
             minimum = medium
        
        else:
            #print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
    return(count)   
    
    
   
   
def score_game (random_predict)->int:
    """Подсчет попыток, за сколько в среднем угадывается число из 1000 попыток

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: число, за которое в среднем угадывается число
    """
    count_ls = [] #пустоя список для хранения числа попыток до угадывания в каждой итерации
    np.random.seed(1) #фиксируем сид для воспроизводимости 
    random_array = np.random.randint(1, 101, size=(10)) #загадан список чисел
    
    for number in random_array:
    
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Алгоритм угадывает число в среднем за {score} попыток')
    return(score)
       
# RUN  
score_game (random_predict)