# Generated by Django 2.0.9 on 2019-01-16 22:00

from django.db import migrations, models
import user.utils


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_govno'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Govno',
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=user.utils.image_name),
        ),
    ]
