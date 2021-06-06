# Generated by Django 3.2 on 2021-06-06 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('ذكر', 'ذكر'), ('انثي', 'انثي')], max_length=40, verbose_name='النوع'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, default='/team-1.jpg', null=True, upload_to='profile/', verbose_name='الصورة الشخصية'),
        ),
    ]
