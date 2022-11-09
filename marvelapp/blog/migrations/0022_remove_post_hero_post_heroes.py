# Generated by Django 4.1.3 on 2022-11-08 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_hero_post_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='hero',
        ),
        migrations.AddField(
            model_name='post',
            name='heroes',
            field=models.ManyToManyField(to='blog.hero'),
        ),
    ]
