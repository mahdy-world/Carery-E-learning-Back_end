# Generated by Django 3.2 on 2021-05-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainer', '0002_auto_20210520_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='email',
        ),
        migrations.AlterField(
            model_name='trainer',
            name='linked_in',
            field=models.CharField(max_length=240, verbose_name='عنوان لينكدان'),
        ),
    ]
