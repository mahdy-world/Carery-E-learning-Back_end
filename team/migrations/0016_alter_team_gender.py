# Generated by Django 3.2 on 2021-05-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0015_alter_team_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='gender',
            field=models.CharField(choices=[('ذكر', 'ذكر'), ('انثي', 'انثي')], max_length=40, verbose_name='النوع'),
        ),
    ]
