from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartametoForm
from applications.persona.models import Empleado 
from .models import Departamento 
from django.urls import reverse_lazy
# Create your views here.

class DepartamentoListView(ListView):
	template_name="departamento/lista.html"
	model=Departamento
	context_object_name='departamento'		

class NewDepartamentoView(FormView):
	template_name='departamento/new_departamento.html'
	form_class=NewDepartametoForm
	success_url=reverse_lazy('departamento_app:nuevo_departamento')


	def form_valid(self, form):
		"""If the form is valid, save the associated model."""
		print("*******estamos en form valid**************")

		depa=Departamento(
				name=form.cleaned_data['departamento'],
				shor_name=form.cleaned_data['shorname'],
			)

		depa.save()

		nombre=form.cleaned_data['nombre']
		apellido=form.cleaned_data['apellidos']
		Empleado.objects.create(
				first_name=nombre,
				last_name=apellido,
				job='1',
				departamento=depa
			)
		


		return super(NewDepartamentoView,self).form_valid(form)
