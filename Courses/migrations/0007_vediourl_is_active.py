# Generated by Django 3.2 on 2021-06-25 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0006_alter_course_student_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='vediourl',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
