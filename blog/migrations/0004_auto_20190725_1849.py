# Generated by Django 2.2.3 on 2019-07-25 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='picture',
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
