# Generated by Django 3.1.6 on 2021-02-20 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('talep', '0003_auto_20210220_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talep',
            name='talepEdenKisi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
