import time
from multiprocessing import Process

from DB.DAO import DAO
from services import Service
from utils import write_dairy, beep
from utils_db import get_all_trainings, read_training, write_training








def main(service: Service) -> None:

    training = service.choosing_training()
    exercises = service.get_exercises_from_training(training.id)

    p = None
    start_time = time.time()

    write_dairy(
        f"{time.asctime(time.localtime(start_time))} Старт тренировки {training.name}\n"
    )

    for i in exercises:
        for at in range(i.attempts):
            print("Упражнение ", i.name)
            print(f"Подход {at + 1} из {i.attempts}")
            print("Предыдущий вес ", i.weight)
            print("Введите вес или ничего при прежнем весе,")
            print("для пропуска подхода введите - ")
            weight_1 = input()
            if weight_1 == "-":
                service.write_dairy(
                    f"{time.asctime(time.localtime(time.time()))} Пропущен {at + 1} подход к упражнению {i.name}\n")
                continue
            elif weight_1 != "":
                i.weight = weight_1
            if p is not None:
                p.join()
            print("выполните", i.rep, "повторений")
            input()

            if not (at + 1 == i.attempts and i is exercises[-1]):
                p = Process(target=beep, args=(training.time_to_breathe,))
                p.start()

            service.write_dairy(
                f"{time.asctime(time.localtime(time.time()))} Выполнен {at + 1} подход к упражнению {i.name}, {i.rep} повторов с весом {i.weight} кг\n")

    d_time = int(time.time() - start_time)
    minute = d_time % 3600 // 60
    minute = minute if minute > 10 else f'0{minute}'

    second = d_time % 60
    second = second if second > 10 else f'0{second}'

    report = f'Время тренировки {d_time // 3600}:{minute}:{second}'
    print(f"Тренировка {training.name} закончена")
    print(report)
    service.write_dairy(
        f"{time.asctime(time.localtime(time.time()))} Тренировка {training.name} закончена. {report}\n\n"
    )
    service.write_training(training, exercises)
    return


if __name__ == '__main__':
    dao = DAO()
    service = Service(dao)
    main(service)
