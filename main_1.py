import time
from multiprocessing import Process

from utils import write_dairy, beep
from utils_db import get_all_trainings, read_training, write_training

all_training = get_all_trainings()
print('Введите id тренировки')
for item in all_training:
    print(item.id, item.name)
print()
training_id = int(input())

for item in all_training:
    if item.id == training_id:
        zz_time = item.time_to_breathe
        training_name = item.name
        break

training = read_training(training_id)

p = None
start_time = time.time()

write_dairy(
    f"{time.asctime(time.localtime(time.time()))} Старт тренировки {training_name}\n"
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
        if p is not None:
            p.join()
        print("выполните", i.rep, "повторений")
        input()

        if not (at + 1 == i.attempts and i is training[-1]):
            p = Process(target=beep, args=(zz_time,))
            p.start()

        write_dairy(
            f"{time.asctime(time.localtime(time.time()))} Выполнен {at+1} подход к упражнению {i.name}, {i.rep} повторов с весом {i.weight} кг\n"
        )
d_time = int(time.time() - start_time)
minute = d_time % 3600 // 60
minute = minute if minute > 10 else f'0{minute}'

second = d_time % 60
second = second if second > 10 else f'0{second}'

report = f'Время тренировки {d_time // 3600}:{minute}:{second}'
print("Тренировка закончена")
print(report)
write_dairy(
    f"{time.asctime(time.localtime(time.time()))} Закончена тренировка {training_name}. {report}\n\n"
)
write_training(training_id, training)
