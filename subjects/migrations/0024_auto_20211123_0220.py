# Generated by Django 3.2.9 on 2021-11-23 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0023_auto_20211123_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_national_id',
        ),
        migrations.AlterField(
            model_name='subject',
            name='doctor_national_id',
            field=models.CharField(max_length=14),
        ),
    ]
