# Generated by Django 4.1.7 on 2023-03-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_advertise_advertise_name_alter_employees_employee_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hoppies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos')),
                ('files', models.FileField(upload_to='files')),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='advertise_relation',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='employee_cv',
        ),
        migrations.DeleteModel(
            name='Advertise',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='employee_Cv',
        ),
        migrations.DeleteModel(
            name='employees',
        ),
    ]
