# Generated by Django 3.0.5 on 2020-04-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20200420_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regis_school',
            name='check_type',
            field=models.BooleanField(default=False),
        ),
    ]
