# Generated by Django 5.1.7 on 2025-03-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selicrate',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
