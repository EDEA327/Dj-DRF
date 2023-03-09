from django.db import models
from applications.departments.models import Department

# Create your models here.
class Skill(models.Model):
    """Model that represents the skills of the employees"""

    #Atributos
    skill_name = models.CharField('Skill', max_length=50)

    #Métodos
    def __str__(self):
        """A method to overwrite __str__() and make the admin panel
        more human readable

        Returns
        -------
        (str)
            The name of the skill object
        """
        return self.skill_name

class Employee(models.Model):
    """Employees model"""
    #Choices
    #! Debe ser una constante (Letras mayusculas)
    #! Debe ser una lista de tuplas
    JOB_CHOICES = [
        ('0','Accountant'),
        ('1','Manager'),
        ('2','Economist'),
        ('3','Other'),
    ]

    #Atributos
    first_name = models.CharField("Names", max_length=50)
    last_name = models.CharField("Last Names", max_length=50)
    job = models.CharField("Job", max_length=50,choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)
    avatar = models.ImageField('Avatar-Image', upload_to='avatars', blank=True, null=True)

    #Meta
    class Meta:
        ordering = ('first_name',)

    #Métodos
    def __str__(self):
        """A method to overwrite __str__() and make the admin panel
        more human readable

        Returns
        -------
        (str)
            The full name of the employee
        """
        return self.first_name + ' ' + self.last_name