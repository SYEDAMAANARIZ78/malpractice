# Generated by Django 4.2 on 2023-04-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_malpracticentry_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malpracticentry',
            name='action',
            field=models.CharField(max_length=50),
        ),
    ]