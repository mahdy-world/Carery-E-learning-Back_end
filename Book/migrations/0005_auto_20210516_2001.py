# Generated by Django 3.2 on 2021-05-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_auto_20210516_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='file_size',
        ),
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default=1, upload_to='files/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]