from django.db import models

# Create your models here.

class Trainer(models.Model):
    Trainer_name = models.CharField(max_length=100, primary_key=True)
    Trainer_subject = models.CharField(max_length=100)
    Trainer_age = models.IntegerField()
    
    def __str__(self):
        return self.Trainer_name
