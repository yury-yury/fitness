from DB.simple import Training, Repetition, Exercise
from database import get_session
import classes.exercise as ex


def get_all_trainings():
    session = next(get_session())
    treins = session.query(Training).order_by(Training.id).all()
    return treins


def read_training(training_id: int) -> list[ex.Exercise]:
    """ """
    session = next(get_session())

    result = list()

    reps = session.query(Repetition).filter(Repetition.training_id == training_id).order_by(Repetition.number).all()

    for item in reps:
        exer = session.get(Exercise, item.exercise_id)

        result.append(ex.Exercise(
            name=exer.name,
            rep=item.repetition,
            attempts=item.set,
            weight=item.weight
        ))
    return result


def write_training(training_id: int, data: list[ex.Exercise]) -> None:
    session = next(get_session())
    for item in data:
        ex = session.query(Exercise).filter(Exercise.name == item.name).first()
        rep = session.query(Repetition).filter(Repetition.training_id == training_id).filter(Repetition.exercise_id == ex.id).first()
        rep.weight = item.weight
        session.add(rep)
        session.commit()




if __name__ == '__main__':
    # print(read_training('тест'))
    # for i in get_all_training():
    #     print(i.id, i.name)
    # for i in read_training(1):
    #     print(i.name, i.attempts, i.rep, i.weight)

    data = read_training(2)
    for item in data:
        item.weight = 10
    write_training(2, data)

