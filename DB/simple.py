from sqlalchemy import create_engine, Column, Integer, String, Text, Float, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship, backref

import classes.exercise as ex
from database import get_session
from settings import settings


# engine = create_engine(settings.database_url, echo=True)


class Base(DeclarativeBase):
    pass


class TargetMuscle(Base):
    __tablename__ = 'training_targetmuscle'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)


class Exercise(Base):
    __tablename__ = 'training_exercise'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    target_muscle = relationship('TargetMuscle', secondary='training_exercise_targetmuscle',
                           backref=backref('exercises', lazy='dynamic'))


# exercise_targetmuscle = Table('training_exercise_targetmuscle', Base.metadata,
#                               Column('id', Integer, primary_key=True),
#                               Column('exercise_id', Integer, ForeignKey('training_exercise.id')),
#                               Column('targetmuscle_id', Integer, ForeignKey('training_targetmuscle.id')))


class ExerciseTargetMuscle(Base):
    __tablename__ = 'training_exercise_targetmuscle'

    id = Column(Integer, primary_key=True)
    exercise_id = Column(Integer, ForeignKey('training_exercise.id'))
    targetmuscle = Column(Integer, ForeignKey('training_targetmuscle.id'))


class Training(Base):
    __tablename__ = 'training_training'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # exercises = models.ManyToManyField(Exercise, through="Repetition", verbose_name='Список упражнений')
    time_to_breathe = Column(Integer)


class Repetition(Base):
    __tablename__ = 'training_repetition'

    id = Column(Integer, primary_key=True)
    training_id = Column(Integer, ForeignKey('training_training.id'))
    number = Column(Integer)
    exercise_id = Column(Integer, ForeignKey('training_exercise.id'))
    set = Column(Integer)
    repetition = Column(Integer)
    weight = Column(Float)


# session = next(get_session())
#
# result = list()
#
# tren = session.query(Training).filter(Training.name == 'Ноги').first()
#
# reps = session.query(Repetition).filter(Repetition.training_id == tren.id).order_by(Repetition.number).all()
#
# for item in reps:
#
#     exer = session.get(Exercise, item.exercise_id)
#
#     result.append(ex.Exercise(
#         name = exer.name,
#         rep=item.repetition,
#         attempts=item.set,
#         weight=item.weight
#     ))
#
# for j in result:
#     print(j.name, j.attempts, j.rep, j.weight)
#

