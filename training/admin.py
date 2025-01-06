from django.contrib import admin

from training.models import TargetMuscle, Exercise, Training, Repetition


class TrainingAdmin(admin.ModelAdmin):
    list_display = ('name', )


class RepetitionAdmin(admin.ModelAdmin):
    list_display: tuple[str, ...] = ('id', 'training', 'exercise', 'set', 'repetition', 'weight',)
    list_filter: tuple[str, ...] = ('training',)


admin.site.register(TargetMuscle)
admin.site.register(Exercise)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Repetition, RepetitionAdmin)
