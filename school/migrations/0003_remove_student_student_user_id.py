# Generated by Django 3.0.5 on 2020-04-14 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200413_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_user_id',
        ),
    ]