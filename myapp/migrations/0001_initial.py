# Generated by Django 4.2 on 2023-04-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Malpracticentry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=50)),
                ('registrationnumber', models.CharField(max_length=50)),
                ('facultyadvisor', models.CharField(max_length=50)),
                ('facultyademail', models.EmailField(max_length=50)),
                ('squadname', models.CharField(max_length=50)),
                ('enquirydate', models.DateField(blank=True, null=True)),
                ('squademail', models.EmailField(max_length=50)),
                ('malpracticedetail', models.CharField(max_length=50)),
                ('examination', models.CharField(max_length=50)),
                ('subjectname', models.CharField(max_length=50)),
                ('subjectcode', models.CharField(max_length=50)),
            ],
        ),
    ]
