# Generated by Django 4.2.10 on 2024-02-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schooladmin', '0003_term_academicyear_current_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='term',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]