"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def binary_tree_predict(number: int = 1, min_number: int = 1, max_number: int =100) -> int:
    """Угадываем число по алгоритму бинарного дерева

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        min_number (int, optional): Нижняя граница интервала. Defaults to 1.
        max_number (int, optional): Верхняя граница интервала. Defaults to 100.
        

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = (max_number - min_number) // 2 + min_number # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        if number > predict_number:
            if min_number == predict_number: # Для number == 100 (100 - 99 // 2 = 0)
                min_number += 1
            else:
                min_number = predict_number # так как число больше продолжаем поиск в верхнем интервале
            continue
        if number < predict_number:
            max_number = predict_number # так как число меньше продолжаем поиск в нижнем интервале
            continue
    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Функция {random_predict.__name__} угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(binary_tree_predict)
