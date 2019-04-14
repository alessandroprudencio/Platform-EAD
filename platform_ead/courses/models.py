from django.db import models

from django.conf import settings

from platform_ead.core.mails import send_email_template

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

class Announcement(models.Model):
        course =  models.ForeignKey(
            Course,
            verbose_name='Curso',
            on_delete = models.CASCADE,
            related_name='announcements')
        title = models.CharField('Titulo', max_length=100)
        content = models.TextField('Conteúdo')

        created_at = models.DateTimeField('Inscrito em ', auto_now_add=True)
        update_at = models.DateTimeField('Inscrição atualizada em ', auto_now=True)

        def __str__(self):
            return self.title

        class Meta:
            verbose_name =  'Anúncio'
            verbose_name_plural = "Anúncios"
            ordering = ['-created_at']

class Comment(models.Model):
        announcement = models.ForeignKey(
            Announcement,
            verbose_name='Anúncio',
            on_delete = models.CASCADE,
            related_name="comments"
            )
        user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            verbose_name='Usuário',
            on_delete = models.CASCADE,
            )
        comment = models.TextField('Comentário')

        created_at = models.DateTimeField('Data do comentário ', auto_now_add=True)
        update_at = models.DateTimeField('Comentário atualizado em ', auto_now=True)

        class Meta:
            verbose_name = 'Comentário'
            verbose_name_plural = 'Comentários'
            ordering = ['created_at']

def post_save_announcement(instance, created, **kwargs):
        subject = instance.title
        context = {
            'announcement':announcement
        }
        template_name='courses/announcement_mail.html'
        enrollments = Enrollment.objects.filter(
            course=announcement.course,
            status=1
            )
        for enrollment in enrollments:
                recipient_list=[enrollment.user.email] 
                send_email_template(subject, template_name, content, announcement)

models.signals.post_save.connect(post_save_announcement,sender=Announcement, dispatch_uid='post_save_announcement')