# Generated by Django 3.2 on 2021-05-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('انثي', 'انثي'), ('ذكر', 'ذكر')], max_length=40, verbose_name='النوع'),
        ),
    ]
