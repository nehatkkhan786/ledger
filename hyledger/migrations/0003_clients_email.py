# Generated by Django 3.2.4 on 2021-06-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyledger', '0002_auto_20210623_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
