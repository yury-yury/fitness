from DB.simple import Training, Repetition, Exercise
from database import Session


class DAO:
    def __init__(self) -> None:
        self.session = next(self._get_session())

    def _get_session(self) -> Session:
        session = Session()
        try:
            yield session
        finally:
            session.close()

    def get_all_trainings(self) -> list[Training]:
        result = self.session.query(Training).order_by(Training.id).all()
        return result

    def get_all_repetition_from_training(self, training_id: int) -> list[Repetition]:
        result = (self.session.query(Repetition).
                  filter(Repetition.training_id == training_id).
                  order_by(Repetition.number).all())
        return result

    def get_exercise(self, exercise_id: int) -> Exercise:
        result = self.session.get(Exercise, exercise_id)
        return result

    def wright_working_weight(self, repetition_id: int, weight: float) -> None:
        (self.session.query(Repetition).filter(Repetition.id == repetition_id).
         update({'weight': weight}, synchronize_session='fetch'))
        self.session.commit()


if __name__ == '__main__':
    dao = DAO()
    dao.wright_working_weight(1, 45.0)


