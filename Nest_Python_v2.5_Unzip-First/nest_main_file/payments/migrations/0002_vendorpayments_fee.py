# Generated by Django 3.1.2 on 2022-05-08 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendorpayments',
            name='fee',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
