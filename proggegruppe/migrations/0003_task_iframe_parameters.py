# Generated by Django 4.2.7 on 2024-07-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proggegruppe', '0002_task_has_ide'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='iframe_parameters',
            field=models.TextField(blank=True, null=True),
        ),
    ]
