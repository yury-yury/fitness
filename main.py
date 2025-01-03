import time
from utils import read_training, write_training, write_dairy

print('Input name of training')
name_training = input()

training = read_training(name_training)
write_dairy(f'{time.asctime(time.localtime(time.time()))} Start training {name_training}\n')
for i in training:
    for at in range(i.attempts):
        print('Упражнение ', i.name)
        print('Подход ', at + 1)
        print('Предыдущий вес ', i.wedth)
        print('Введите вес или ничего при прежнем весе')
        weth_1 = input()
        if weth_1 != '':
            i.wedth = weth_1
        print('выполните', i.rep, 'повторений')
        input()
        write_dairy(f'{time.asctime(time.localtime(time.time()))} Выполнен {at+1} подход к упражнению {i.name}, {i.rep} повторов с весом {i.wedth} кг\n')
print('Тренировка закончена')
write_dairy(f'{time.asctime(time.localtime(time.time()))} Finished training {name_training}\n')
write_training(name_training, training)
