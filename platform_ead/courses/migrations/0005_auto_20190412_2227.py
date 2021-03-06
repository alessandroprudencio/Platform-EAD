# Generated by Django 2.1.7 on 2019-04-12 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_auto_20190412_0850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('content', models.TextField(verbose_name='Conteúdo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Inscrito em ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Inscrição atualizada em ')),
            ],
            options={
                'verbose_name_plural': 'Anúncios',
                'verbose_name': 'Anúncio',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comentário')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data do comentário ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Comentário atualizado em ')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='courses.Announcement', verbose_name='Anúncio')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name_plural': 'Comentários',
                'verbose_name': 'Comentário',
                'ordering': ['created_at'],
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Autor '),
        ),
        migrations.AlterField(
            model_name='course',
            name='introductory_video',
            field=models.FileField(null=True, upload_to='courses/videos', verbose_name='Video de Introdução'),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, verbose_name='Preço'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='Curso'),
        ),
    ]
