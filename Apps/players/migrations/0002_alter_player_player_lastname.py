# Generated by Django 4.0.3 on 2022-04-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_lastname',
            field=models.CharField(max_length=50, verbose_name='Lastname'),
        ),
    ]
