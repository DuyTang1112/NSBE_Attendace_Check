# Generated by Django 2.0.2 on 2018-03-01 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='secretkey',
            field=models.CharField(default='duy', max_length=50),
            preserve_default=False,
        ),
    ]
