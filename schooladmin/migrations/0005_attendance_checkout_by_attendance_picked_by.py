# Generated by Django 4.2.10 on 2024-02-24 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schooladmin', '0004_alter_term_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='checkout_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendance',
            name='picked_by',
            field=models.TextField(blank=True, null=True),
        ),
    ]