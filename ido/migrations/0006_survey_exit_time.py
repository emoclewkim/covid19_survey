# Generated by Django 3.1.1 on 2020-09-23 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ido', '0005_auto_20200916_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='exit_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
