# Generated by Django 4.2.7 on 2024-07-23 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proggegruppe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
