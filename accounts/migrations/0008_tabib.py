# Generated by Django 3.2.9 on 2021-11-26 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tabib_profile', to='accounts.profile')),
            ],
        ),
    ]
