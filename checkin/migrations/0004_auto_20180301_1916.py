# Generated by Django 2.0.2 on 2018-03-02 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0003_checkentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkentry',
            name='timeout',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='timeout',
            field=models.DateTimeField(null=True),
        ),
    ]
