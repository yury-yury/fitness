from utils import read_training, write_training

print('Input name of training')
name_training = input()

training = read_training(name_training)
# print(training)
for i in training:
    for at in range(i.attempts):
        print('Exercise ', i.name)
        print('Attempt ', at + 1)
        print('Предыдущий вес ', i.wedth)
        print('Введите вес или ничего при прежнем весе')
        weth_1 = input()
        if weth_1 != '':
            i.wedth = weth_1
        print('выполните', i.rep, 'повторений')
        input()
print('Тренировка закончена')
write_training(name_training, training)
"""
except:
    print('Ошибка при открытии файла')
"""