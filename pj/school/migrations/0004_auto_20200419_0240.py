# Generated by Django 3.0.5 on 2020-04-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_score_check_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='check_type',
            field=models.BooleanField(default=False),
        ),
    ]