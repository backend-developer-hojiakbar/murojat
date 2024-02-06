# Generated by Django 4.2.1 on 2024-02-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=23)),
                ('surname', models.CharField(max_length=30)),
                ('series', models.CharField(max_length=2)),
                ('number', models.IntegerField()),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]