# Generated by Django 2.2.3 on 2020-08-11 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200610_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
    ]
