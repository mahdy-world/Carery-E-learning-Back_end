
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [

        ('accounts', '0024_feedback'),

        ('accounts', '0024_alter_student_gender'),

    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',

            field=models.CharField(choices=[('ذكر', 'ذكر'), ('انثي', 'انثي')], max_length=40, verbose_name='النوع'),

            field=models.CharField(choices=[('انثي', 'انثي'), ('ذكر', 'ذكر')], max_length=40, verbose_name='النوع'),

        ),
    ]
