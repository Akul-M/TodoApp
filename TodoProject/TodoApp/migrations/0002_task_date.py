# Generated by Django 4.1.3 on 2023-07-21 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1997-02-05'),
            preserve_default=False,
        ),
    ]
