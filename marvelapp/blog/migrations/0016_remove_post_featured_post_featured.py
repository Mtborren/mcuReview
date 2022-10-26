# Generated by Django 4.1.1 on 2022-10-25 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured',
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.ManyToManyField(to='blog.featured'),
        ),
    ]
