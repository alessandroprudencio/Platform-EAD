# Generated by Django 2.1.7 on 2019-04-12 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='introductory_video',
            field=models.FileField(null=True, upload_to='courses/videos'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=1, verbose_name='Situação'),
        ),
    ]