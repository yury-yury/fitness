from utils import read_training, write_training

print('Input name of training')
name_training = input()

training = read_training(name_training)
# print(training)
for i in range(len(training)):
    [exes, rep, attem, weth] = training[i]
    for at in range(attem):
        print('Exercise ', exes)
        print('Attempt ', at + 1)
        print('Предыдущий вес ', weth)
        print('Введите вес или ничего при прежнем весе')
        weth_1 = input()
        if weth_1 != '':
            weth = weth_1
            training[i][3] = weth
        print('выполните', rep, 'повторений')
        input()
print('Тренировка закончена')
write_training(name_training, training)
"""
except:
    print('Ошибка при открытии файла')
"""