import numpy as np
number = np.random.randint(1,101)  # загадываем число
count = 0
while True:
    count += 3
    predict_number = int(input("Угадай число от 1 до 100: "))
    if predict_number<number:
        print("Число должно быть больше")
    elif predict_number>number:
        print("Число должно быть меньше вообще")
    else:
        print("Вы угадали число - это {}, количество попыток {}". format(number, count))
        break  # Конец игры
    
    
    