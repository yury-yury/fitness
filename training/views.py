from django.shortcuts import render

def index(request, name_training):
    print(name_training)
    return render(request, 'training/my_training.html')
