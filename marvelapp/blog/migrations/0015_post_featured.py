# Generated by Django 4.1.1 on 2022-10-20 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.CharField(default='Unfeatured', max_length=255),
        ),
    ]
