# Generated by Django 4.1.7 on 2023-02-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Board_name', models.CharField(max_length=100)),
                ('created_by', models.CharField(max_length=100)),
                ('created_date', models.DateField()),
                ('created_at', models.TimeField()),
            ],
        ),
    ]