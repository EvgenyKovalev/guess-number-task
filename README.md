# Проект 0. Угадай число

## Оглавление  
[1. Описание проекта](#Описание-проекта)  
[2. Какой кейс решаем?](#Какой-кейс-решаем)  
[3. Краткая информация о данных](#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](#Этапы-работы-над-проектом)  
[5. Результат](#Результат)    
[6. Выводы](#Выводы) 

### Описание проекта    
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](_)


### Какой кейс решаем?    
Нужно написать программу, которая угадывает число за минимальное число попыток

**Условия соревнования:**  
- Компьютер загадывает целое число от 0 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

**Метрика качества**     
Результаты оцениваются по среднему количеству попыток при 1000 повторений

**Что практикуем**     
Учимся писать хороший код на python


### Краткая информация о данных

Данные генерируем при помощи функции randint из модуля numpy.
   
:arrow_up:[к оглавлению](.README.md#Оглавление)


### Этапы работы над проектом  

Используя код функции random_predict из базового решения задачи была реализована функция binary_tree_predict использующая алгоритм бинарного дерева для поиска загаданного числа.

Фунция binary_tree_predict была протестирована в сравнении с фунцией random_predict. В результате тестирования получены следующие реузльтаты:
Функция random_predict угадывает число в среднем за:100 попыток
Функция binary_tree_predict угадывает число в среднем за:5 попыток

Для обеспечения воспроизводимости кода командой pip freeze > requirements.txt был создан файл requriments.txt и размещен в папке проекта.

Написаны комметарии в соответствии с PEP8.

Произведно документтирование проекта.

Проект загружен на GitHub.

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Результаты:  

Функция random_predict угадывает число в среднем за:100 попыток
Функция binary_tree_predict угадывает число в среднем за:5 попыток

:arrow_up:[к оглавлению](.README.md#Оглавление)


### Выводы:  

Случайный перебор значений в 20 раз меннее эффективен в сравнении с алгоритмом бинарного дерева на интервале [1..100]

:arrow_up:[к оглавлению](.README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
