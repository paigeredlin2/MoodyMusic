# Generated by Django 5.1.3 on 2024-12-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='request_remarks',
            field=models.CharField(max_length=10000),
        ),
    ]
