# Generated by Django 4.1.4 on 2023-02-11 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1992-05-06'),
            preserve_default=False,
        ),
    ]
