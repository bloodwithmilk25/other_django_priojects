# Generated by Django 2.1.1 on 2018-09-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('position', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
