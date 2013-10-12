from django.db import models

class Professor(models.Model):
	nome = models.CharField(max_length = 100)
	notaCat1 = models.FloatField(default = 0)
	notaCat2 = models.FloatField(default = 0)
	notaCat3 = models.FloatField(default = 0)
	numVotos = models.IntegerField(default = 0)
	media = models.FloatField(default = 0)
	alunos = models.CommaSeparatedIntegerField(max_length = 20000)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.nome

# Create your models here.
