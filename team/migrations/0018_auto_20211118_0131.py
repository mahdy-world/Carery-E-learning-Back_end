# Generated by Django 2.2 on 2021-11-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0017_auto_20210523_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]