# Generated by Django 4.2 on 2023-04-24 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_action_malpracticentry_actiontaken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='malpracticentry',
            name='actiontaken',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
