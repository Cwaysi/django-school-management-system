# Generated by Django 4.2.10 on 2024-03-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooladmin', '0005_attendance_checkout_by_attendance_picked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='checkin_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
