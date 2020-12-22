# Generated by Django 3.0 on 2020-09-09 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bathroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bath_name', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=2)),
                ('current_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('matno', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=30)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]