# Generated by Django 4.2.1 on 2024-02-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_contact_number_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
