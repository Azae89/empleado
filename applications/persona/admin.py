from django.contrib import admin
from .models import Empleado,Habilidades
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field

# Register your models here.

admin.site.register(Habilidades) 


class EmpleadoResource(resources.ModelResource):
  full_name = Field(column_name='first_name')

  class Meta:
    model = Empleado
    fields = ('first_name', 'last_name', 'departamento', )
   

  def dehydrate_full_name(self, student):
    return f'{student.first_name} {student.last_name} {student.departamento}'

class EmpleadoExportAdmin(ImportExportModelAdmin):
    resource_class = EmpleadoResource

class EmpleadoAdmin(ImportExportModelAdmin):
	list_display=(
		'id',
		'first_name',
		'last_name',
		'departamento',
		'job',
		'full_name',

		)


	def full_name(self,obj):
		#Toda la operacion que necesite

		return obj.first_name + " " + obj.last_name


	search_fields=(
		'first_name',
		)
	list_filter=('departamento','job','habilidades')
	filter_horizontal=('habilidades',)

admin.site.register(Empleado,EmpleadoAdmin) 

 


		
