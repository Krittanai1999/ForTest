# Generated by Django 3.0.5 on 2020-04-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20200414_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='room',
            field=models.CharField(max_length=255),
        ),
    ]
