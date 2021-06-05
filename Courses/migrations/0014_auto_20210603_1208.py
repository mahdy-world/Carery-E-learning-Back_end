# Generated by Django 3.2 on 2021-06-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0013_auto_20210603_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image1',
            field=models.ImageField(default=1, upload_to='summary/', verbose_name='الصورة الاولي'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='image2',
            field=models.ImageField(default=1, upload_to='summary/', verbose_name='الصورة الثانية'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='image3',
            field=models.ImageField(default=1, upload_to='summary/', verbose_name='الصورة الثالثة'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='image4',
            field=models.ImageField(default=1, upload_to='summary/', verbose_name='الصورة الرابعة'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='image5',
            field=models.ImageField(default=1, upload_to='summary/', verbose_name='الصورة الخامسة'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='p1',
            field=models.CharField(default=1, max_length=100, verbose_name='العنوان الفرعي الاول'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='p2',
            field=models.CharField(default=1, max_length=100, verbose_name='العنوان الفرعي الثاني'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='p3',
            field=models.CharField(default=1, max_length=100, verbose_name='العنوان الفرعي الثالث'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='p4',
            field=models.CharField(default=1, max_length=100, verbose_name='العنوان الفرعي الرابع'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='p5',
            field=models.CharField(default=1, max_length=100, verbose_name='العنوان الفرعي الخامس'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='title1',
            field=models.CharField(default=1, max_length=50, verbose_name='العنوان الاول'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='title2',
            field=models.CharField(default=1, max_length=50, verbose_name='العنوان الثاني'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='title3',
            field=models.CharField(default=1, max_length=50, verbose_name='العنوان الثالث'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='title4',
            field=models.CharField(default=1, max_length=50, verbose_name='العنوان الرابع'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='title5',
            field=models.CharField(default=1, max_length=50, verbose_name='العنوان الخامس'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='SummaryCourse',
        ),
    ]
