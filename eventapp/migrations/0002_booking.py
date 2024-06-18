# Generated by Django 4.2.1 on 2023-10-06 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cus_name', models.CharField(max_length=55)),
                ('cus_ph', models.CharField(max_length=12)),
                ('Booking_date', models.DateField()),
                ('booked_one', models.DateField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventapp.event')),
            ],
        ),
    ]
