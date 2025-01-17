from django.shortcuts import render

from training.models import Training


def index(request, id_training):
    print(id_training)
    my_training = Training.objects.get(pk=id_training)
    print(my_training)
    return render(request, 'training/my_training.html')
