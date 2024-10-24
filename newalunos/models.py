from django.db import models

class Alunos(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    matricula = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

# Create your models here.
