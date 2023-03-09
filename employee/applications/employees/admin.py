from django.contrib import admin
from .models import Employee,Skill

# Register your models here.

admin.site.register(Skill)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'department',
        'job',
        'full_name',
    )
    search_fields = ('first_name',)
    list_filter = ('job','skills')
    #
    ## Solo funciona para los campos M2M
    filter_horizontal = ('skills',)

    #Metodos
    def full_name(self,obj):
    #*obj trae cada registro que se está iterando en el admin
        return obj.first_name + ' ' + obj.last_name

admin.site.register(Employee,EmployeeAdmin)