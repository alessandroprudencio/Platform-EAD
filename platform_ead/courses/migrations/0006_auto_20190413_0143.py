# Generated by Django 2.1.7 on 2019-04-13 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20190412_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='courses.Course', verbose_name='Curso'),
        ),
    ]