# Generated by Django 4.1.5 on 2023-03-08 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='short_name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Alias'),
        ),
    ]
