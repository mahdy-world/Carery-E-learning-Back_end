# Generated by Django 3.2 on 2021-05-20 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trainer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='phone',
        ),
        migrations.AddField(
            model_name='trainer',
            name='job',
            field=models.CharField(max_length=50, null=True, verbose_name='الوظيفة'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='البريد الالكتروني'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='facebook',
            field=models.CharField(max_length=240, verbose_name='عنوان الفيس بوك'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='image',
            field=models.ImageField(upload_to='traniers/', verbose_name='الصورة'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='instagram',
            field=models.CharField(max_length=240, verbose_name='عنوان الانستجرام'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='linked_in',
            field=models.CharField(max_length=240, verbose_name='عنوان التويتر'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(max_length=30, verbose_name='الاسم'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='twitter',
            field=models.CharField(max_length=240, verbose_name='عنوان التويتر'),
        ),
    ]