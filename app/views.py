from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *


class Trainer_list(ListView):
    model = Trainer    ## --> it will create a queryset automatically
    template_name = 'Trainer_list.html'
    context_object_name = 'tl'  ## --> in fbv we will store like this --> tl=Trainer.object.all()
    
    ## for specific details we will use queryset
    ## queryset = Trainer.objects.filter(Trainer_name='Harshad')
    
    ordering=['Trainer_name']