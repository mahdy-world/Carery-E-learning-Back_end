# Generated by Django 3.2 on 2021-06-06 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_feedback'),
        ('Trainer', '0003_auto_20210520_1440'),
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='الاسم')),
                ('address', models.CharField(max_length=150, verbose_name='العنوان')),
                ('phone', models.CharField(max_length=150, verbose_name='رقم الموبيل')),
                ('logo', models.ImageField(upload_to='sponsers/', verbose_name='الشعار')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
        migrations.AddField(
            model_name='course',
            name='detail_image',
            field=models.ImageField(default=1, upload_to='courses/', verbose_name='صورة الوصف'),
            preserve_default=False,
        ),
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
        migrations.AddField(
            model_name='course',
            name='trainer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Trainer_name', to='Trainer.trainer', verbose_name='اسم المدرب'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='count_lesson',
            field=models.CharField(max_length=100, verbose_name='عدد الدروس'),
        ),
        migrations.CreateModel(
            name='VedioUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان الفيديو')),
                ('url', models.CharField(max_length=500, verbose_name='رابط الفيديو')),
                ('shows', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vedio_courses', to='Courses.course', verbose_name='الكورس')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, '1 - Tarsh'), (2, '2 - Horrible'), (3, '3 - Terrible'), (4, '4 - Bad'), (5, '5 - Ok'), (6, '6 - Watchable'), (7, '7 - Good'), (8, '8 - Very Good'), (9, '9 - Perfect'), (10, '10 - Master Piece')])),
                ('text', models.TextField(max_length=2000)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='CoursesRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_register', to='Courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_register', to='accounts.student')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='sponsers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='course_sponsers', to='Courses.sponsers', verbose_name='الرعاة'),
            preserve_default=False,
        ),
    ]
