# Generated by Django 3.0.5 on 2020-04-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20200414_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='weekday',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=255),
        ),
    ]