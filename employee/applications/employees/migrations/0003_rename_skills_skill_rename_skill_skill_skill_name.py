# Generated by Django 4.1.7 on 2023-03-09 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_skills_alter_employee_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='skill_name',
        ),
    ]