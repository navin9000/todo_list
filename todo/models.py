from django.db import models

class todomodel(models.Model):
	todo=models.CharField(max_length=300)

	def __str__(self):
		return self.todo
	