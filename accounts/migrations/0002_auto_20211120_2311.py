# Generated by Django 3.2.9 on 2021-11-20 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='profile',
            name='accounts_profile_national_id_length',
        ),
        migrations.AlterField(
            model_name='profile',
            name='national_id',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddConstraint(
            model_name='profile',
            constraint=models.CheckConstraint(check=models.Q(('phone_number__length__gte', 11)), name='accounts_profile_phone_number_length'),
        ),
    ]
