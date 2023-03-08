from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Alias', max_length=20)
    anulate = models.BooleanField('Anulate', default=False)

    def __str__(self):
        return self.name