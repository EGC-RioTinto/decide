# Generated by Django 2.0 on 2021-01-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0010_merge_20210118_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='url',
            field=models.CharField(help_text='http://localhost:8000/booth/', max_length=40),
        ),
    ]