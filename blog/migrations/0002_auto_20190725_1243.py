# Generated by Django 2.2.3 on 2019-07-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='blog_img/'),
        ),
    ]
