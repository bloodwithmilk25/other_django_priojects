# Generated by Django 2.0.9 on 2019-01-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, verbose_name='date of birth'),
        ),
    ]
