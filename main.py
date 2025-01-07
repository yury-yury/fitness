import time
from multiprocessing import Process

from utils import read_training, write_training, write_dairy, beep

print("Input name of training")
name_training = input()
print("Введите желаемое время отдыха между подходами")
zz_time = int(input())

training = read_training(name_training)
write_dairy(
    f"{time.asctime(time.localtime(time.time()))} Start training {name_training}\n"
)
for i in training:
    for at in range(i.attempts):
        print("Упражнение ", i.name)
        print(f"Подход {at + 1} из {i.attempts}")
        print("Предыдущий вес ", i.weight)
        print("Введите вес или ничего при прежнем весе,")
        print("для пропуска подхода введите - " )
        weight_1 = input()
        if weight_1 == "-":
            write_dairy(f"{time.asctime(time.localtime(time.time()))} Пропущен {at+1} подход к упражнению {i.name}\n")
            continue
        elif weight_1 != "":
            i.weight = weight_1
        print("выполните", i.rep, "повторений")
        input()

        p = Process(target=beep, args=(zz_time,))
        p.start()

        write_dairy(
            f"{time.asctime(time.localtime(time.time()))} Выполнен {at+1} подход к упражнению {i.name}, {i.rep} повторов с весом {i.weight} кг\n"
        )
print("Тренировка закончена")
write_dairy(
    f"{time.asctime(time.localtime(time.time()))} Finished training {name_training}\n\n"
)
write_training(name_training, training)
