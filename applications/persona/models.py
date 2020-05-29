from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
	skill=models.CharField('Habilidad', max_length=60)
	class Meta:
		verbose_name = 'Habilidad'
		verbose_name_plural="Habilidades Empleado"
		ordering = ['skill']


	def __str__(self):
		return str(self.id)+" "+self.skill

# Create your models here.

class Empleado(models.Model):
	""" Modelo para tabla empleado"""
	JOB_CHOICES=(
		('0','CONTADOR'),
		('1','ADMISTRADOR'),
		('2','ECONOMISTA'),
		('3','OTRO'),
		
		)
	#Contador
	#Administrador 
	#Economista
	#Otro
	first_name=models.CharField('Nombre', max_length=60)
	last_name=models.CharField('Apellidos', max_length=60)
	full_name=models.CharField(
		'Nombres completos',
		 max_length=120,
		 blank=True
		 )
	job=models.CharField('Trabajo',max_length=1, choices=JOB_CHOICES)
	departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE)
	avatar=models.ImageField(upload_to='empleado',blank=True,null=True)
	habilidades=models.ManyToManyField(Habilidades)
	hoja_vida=RichTextField()

	class Meta:
		verbose_name = 'Empleados del area'
		verbose_name_plural="Empleados de las àreas"
		ordering = ['first_name']
		#unique_together=('name','shor_name')

	def __str__(self):
		return str(self.id) + "-" + self.first_name + "-" +self.last_name
