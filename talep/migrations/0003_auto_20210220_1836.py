# Generated by Django 3.1.6 on 2021-02-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talep', '0002_auto_20210220_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talep',
            name='talepEdenKisi',
            field=models.CharField(default='', max_length=100, verbose_name='Talep Eden'),
        ),
    ]
