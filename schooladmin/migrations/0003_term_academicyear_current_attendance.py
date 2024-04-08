# Generated by Django 4.2.10 on 2024-02-19 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schooladmin', '0002_students_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('current', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='academicyear',
            name='current',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(max_length=100)),
                ('check_in_date', models.DateField(blank=True, null=True)),
                ('check_in_time', models.TimeField(blank=True, null=True)),
                ('check_out_date', models.DateField(blank=True, null=True)),
                ('check_out_time', models.TimeField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('academicYear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schooladmin.academicyear')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schooladmin.students')),
                ('term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='schooladmin.term')),
            ],
        ),
    ]