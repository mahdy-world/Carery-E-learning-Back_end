# Generated by Django 2.2 on 2021-11-17 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0011_book_created_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
