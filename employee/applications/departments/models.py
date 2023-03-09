from django.db import models

# Create your models here.
class Department(models.Model):
    """Model for Departments"""

    #Atributos
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Alias', max_length=20, unique=True)
    anulate = models.BooleanField('Anulate', default=False)

    #Métodos
    def __str__(self):
        """A method to overwrite __str__() and make the admin panel
        more human readable.

        Returns
        -------
        _str_
            _The name of Department_
        """
        return self.name