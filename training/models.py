from django.db import models


class TargetMuscle(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Функции мышцы')

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Целевая мышца"
        verbose_name_plural: str = "Целевые мышцы"

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    target_muscle = models.ManyToManyField(TargetMuscle, verbose_name='Список целевых мышц')

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Упражнение"
        verbose_name_plural: str = "Упражнения"

    def __str__(self):
        return self.name


class Training(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название тренировки')
    exercises = models.ManyToManyField(Exercise, through="Repetition", verbose_name='Список упражнений')
    time_to_breathe = models.IntegerField()

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Тренировка"
        verbose_name_plural: str = "Тренировки"

    def __str__(self):
        return self.name


class Repetition(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE, verbose_name='Tренировка')
    number = models.IntegerField(verbose_name='Порядковый номер в тренировке')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, verbose_name='Упражнение')
    set = models.IntegerField(verbose_name='Количество подходов')
    repetition = models.IntegerField(verbose_name='Количество повторений')
    weight = models.FloatField(blank=True, null=True, verbose_name='Рабочий вес')

    def __str__(self):
        return self.training.name + ' ' + self.exercise.name

    class Meta:
        """
        The Meta class contains the common name of the model instance in the singular and plural used
        in the administration panel.
        """
        verbose_name: str = "Повторения"
        verbose_name_plural: str = "Повторения"
        ordering = ['number', ]
