# Generated by Django 3.1.2 on 2022-05-06 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_auto_20220506_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='Work_time',
            field=models.CharField(max_length=150),
        ),
    ]
