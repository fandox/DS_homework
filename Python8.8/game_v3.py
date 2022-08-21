"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

from game_v2 import score_game 


def binary_predict(number: int = 1) -> int:
    """Угадываем число бинарным поиском

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left=0 #левая граница
    right=101 #правая граница

    while True:
        count += 1
        predict_number = (left+right)//2  # предполагаемое число
        if predict_number < number:
            left=predict_number # сдвигаем левую границу если число больше
        elif predict_number > number:
            right=predict_number # сдвигаем левую границу если число меньше
        else:
            break  # выход из цикла если угадали
    return count

if __name__ == "__main__":
    # RUN
    score_game(binary_predict) # проверяем бинарный поиск на 1000 испытаний