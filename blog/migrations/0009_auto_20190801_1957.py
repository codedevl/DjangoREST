# Generated by Django 2.2.3 on 2019-08-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190725_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='discription',
            field=models.CharField(default='', max_length=20000),
        ),
    ]
