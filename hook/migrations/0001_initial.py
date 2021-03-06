# Generated by Django 3.2.9 on 2021-11-23 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Cell_number', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Prefered_Comminication', models.CharField(choices=[('P', 'Phone'), ('E', 'Email')], default='Phone', max_length=6)),
                ('Consent', models.BooleanField(default=False)),
                ('Entry_counter', models.IntegerField(default=1)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
