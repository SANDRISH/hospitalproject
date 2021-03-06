# Generated by Django 3.0.6 on 2020-05-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200524_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_hr',
            field=models.BooleanField(default=False, verbose_name='HR Status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_Patient',
            field=models.BooleanField(default=True, verbose_name='Patient Status'),
        ),
    ]
