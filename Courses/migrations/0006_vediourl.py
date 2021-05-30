# Generated by Django 3.2 on 2021-05-29 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0005_auto_20210529_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='VedioUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان الفيديو')),
                ('url', models.CharField(max_length=500, verbose_name='رابط الفيديو')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vedio_courses', to='Courses.course', verbose_name='الكورس')),
            ],
        ),
    ]