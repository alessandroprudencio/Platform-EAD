# Generated by Django 2.1.7 on 2019-04-14 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20190413_0143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome da Lissão')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='Número (ordem)')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Data de Liberação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data do comentário ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Comentário atualizado em ')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.Course', verbose_name='Curso')),
            ],
            options={
                'ordering': ['number'],
                'verbose_name_plural': 'Aulas',
                'verbose_name': 'Aula',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome da Aula')),
                ('embedded', models.TextField(blank=True, verbose_name='Video Embedded')),
                ('file', models.FileField(blank=True, null=True, upload_to='lessons/materials')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='courses.Lesson', verbose_name='aula')),
            ],
            options={
                'verbose_name_plural': 'Materiais',
                'verbose_name': 'Material',
            },
        ),
    ]
