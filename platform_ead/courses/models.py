from django.db import models

from django.conf import settings

class CourseManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
           models.Q(name__icontains=query) | \
           models.Q(name__icontains=query))

class Course(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Categoria')
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField('Data de Inicio', null=True, blank=True)
    image = models.ImageField(upload_to='courses/image',null=True, blank=True, verbose_name="Image")
    author = models.CharField('Autor ',max_length=100, blank=False, null=False)
    price =  models.DecimalField(max_digits=6, decimal_places=2, blank=True, default = 0, verbose_name="Preço")
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)
    introductory_video= models.FileField(upload_to='courses/videos', null=True, verbose_name="Video de Introdução")


    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/cursos/%s" %(self.name)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ['name']

class Enrollment(models.Model):

        STATUS_CHOICES = (
            (0, 'Pendente'),
            (1, 'Aprovado'),
            (2, 'Cancelado')
        )

        user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            verbose_name='Usuário',
            on_delete = models.CASCADE,
            related_name='enrollments')

        course =  models.ForeignKey(
            Course,
            verbose_name='Curso',
            on_delete = models.CASCADE,
            related_name='enrollments')

        status = models.IntegerField(
            'Situação',
            choices=STATUS_CHOICES,
            default=1,
            blank=True)

        created_at = models.DateTimeField('Inscrito em ', auto_now_add=True)
        update_at = models.DateTimeField('Inscrição atualizada em ', auto_now=True)

        def active(self):
            self.status = 1
            self.save()

        def is_approved(self):
            return self.status == 1

        class Meta:
            verbose_name = 'Inscrição'
            verbose_name_plural = 'Inscrições'
            unique_together = (('user','course'),)
