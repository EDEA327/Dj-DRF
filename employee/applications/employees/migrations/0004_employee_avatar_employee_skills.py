# Generated by Django 4.1.7 on 2023-03-09 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_rename_skills_skill_rename_skill_skill_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Avatar-Image'),
        ),
        migrations.AddField(
            model_name='employee',
            name='skills',
            field=models.ManyToManyField(to='employees.skill'),
        ),
    ]