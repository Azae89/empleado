from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	TemplateView,
	UpdateView,
	DeleteView,
	)
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.

class InicioView(TemplateView):
	"""Vista que carga la pagina de inicio"""
	template_name="inicio.html"


class ListAllEmpleados(ListView):
	template_name='persona/list_all.html'
	#model=Empleado
	paginate_by=2
	#ordering='first_name'
	#context_object_name='lista'

	def get_queryset(self):
		palabra_clave=self.request.GET.get("kword",'')
		lista=Empleado.objects.filter(
		full_name__icontains=palabra_clave
		)
		return lista



class ListByAreaEmpleado(ListView):
	"""List de empleados de un àrea"""
	template_name='persona/list_by_area.html'
	context_object_name='empleados'

	def get_queryset(self):

		area=self.kwargs['shorname']
		lista=Empleado.objects.filter(
		departamento__shor_name=area
		)

		return lista


class ListaEmpleadosAdmin(ListView):
	template_name='persona/lista_empleados.html'
	model=Empleado
	paginate_by=10
	ordering='first_name'
	context_object_name='empleados'


class ListEmpleadosByword(ListView):
	"""List de empleados por palabra clave"""
	template_name="empleado/by_word.html"
	context_object_name='empleados'

	def get_queryset(self):
		palabra_clave=self.request.GET.get("kword",'')
		print("=======",palabra_clave)

		lista=Empleado.objects.filter(
		first_name=palabra_clave
		)

		return lista

class ListHabilitadesEmpleado(ListView):
	template_name="empleado/habilidades.html"
	context_object_name="habilidades"

	def get_queryset(self):
		palabra_clave=self.request.GET.get("kword",'')
		empleado=Empleado.objects.get(first_name=palabra_clave)
		lista=empleado.habilidades.all()

		return lista

class EmpleadoDetailView(DetailView):
	model=Empleado
	template_name="persona/detail_empleado.html"

	def get_context_data(self,**kwargs):
		context=super(EmpleadoDetailView,self).get_context_data(**kwargs)
		context['titulo']='Empleado de mes'

		return context

class EmpleadoCreateView(CreateView):
	template_name='empleado/add.html'
	model=Empleado
	form_class=EmpleadoForm
	success_url=reverse_lazy('empleado_app:empleados_admin')

	def form_valid(self, form):
		"""If the form is valid, save the associated model."""
		empleado=form.save(commit=False)
		empleado.full_name=empleado.first_name+" "+empleado.last_name
		empleado.save()

		return super(EmpleadoCreateView,self).form_valid(form)



class SuccessView(TemplateView):
	template_name="empleado/success.html"

class EmpleadoUpdateView(UpdateView):
	model= Empleado
	template_name="empleado/update.html"
	fields=['first_name',
			'last_name',
			'job',
			'departamento',
			'habilidades',
			]
	success_url=reverse_lazy('empleado_app:empleados_admin')

	def post(self,request,*args,**kwargs):
		self.objects=self.get_object()
		print("*************METODO POST*************")
		print("*************METODO POST*************")
		print(request.POST)
		print(request.POST['last_name'])
		print("***********************************")
		return super().post(request,*args,**kwargs)

	def form_valid(self, form):
		"""If the form is valid, save the associated model."""
		print("*************METODO FORM VALID*************")
		print("***********************************")
		return super(EmpleadoUpdateView,self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
	model=Empleado
	template_name="empleado/delete.html"
	success_url=reverse_lazy('empleado_app:empleados_admin')


