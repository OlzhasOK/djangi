# Generated by Django 4.0 on 2024-02-24 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='', verbose_name='post/imgs/'),
        ),
    ]
