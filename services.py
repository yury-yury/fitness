import time

from playsound import playsound

from DB.DAO import DAO
from DB.simple import Training
import classes.exercise as ex


class Service:

    def __init__(self, dao: DAO):
        self.dao = dao
        self.dairy = "storage/training_dairy.txt"
        self.sound = 'static/vyistrel-pistoleta-36125.mp3'

    def choosing_training(self) -> Training:
        print('Выберите id тренировки:')
        trens = self.dao.get_all_trainings()
        for tren in trens:
            print(tren.id, tren.name)
        training_id = int(input())
        for tren in trens:
            if tren.id == training_id:
                training = tren
                break
        return training

    def get_exercises_from_training(self, training_id: int) -> list[ex.Exercise]:
        repetitions = self.dao.get_all_repetition_from_training(training_id)
        result = list()
        for item in repetitions:
            exercise = self.dao.get_exercise(item.exercise_id)
            result.append(ex.Exercise(
                id=item.id,
                name=exercise.name,
                rep=item.repetition,
                attempts=item.set,
                weight=item.weight
            ))
        return result

    def write_dairy(self, data: str) -> None:
        """
        The write_dairy function takes as a positional argument the text of an entry in the training diary,
        in the form of a string. When called, it opens the training diary file, adds an entry to the file,
        and closes the file.
        """
        with open(self.dairy, "a", encoding="utf-8") as file:
            file.write(data)

    def beep(self, t: int) -> None:
        """
        The beep function takes as a positional argument the value of the rest time between sets in seconds,
        as an integer. When a call is made after the end of the rest period, an audio signal is played.
        """
        time.sleep(t)
        playsound(self.sound)

    def write_training(self, training: Training, exercises: list[ex.Exercise]) -> None:
        for exercise in exercises:
            self.dao.wright_working_weight(exercise.id, exercise.weight)


if __name__ == '__main__':
    dao = DAO()
    service = Service(dao)
    training = service.choosing_training()
    exercises = service.get_exercises_from_training(2)
    exercises[0].weight = 70
    service.write_training(training, exercises)

