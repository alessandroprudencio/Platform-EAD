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
    author = models.CharField('Author ',max_length=100, blank=False, null=False)
    price = models.DecimalField('Preço do curso', max_digits=10, decimal_places=2, default=0, blank=True)
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)

    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/cursos/%s" %(self.slug)

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
        on_delete = models.PROTECT,
        related_name="enrollments",
    )        
    
    course = models.ForeignKey(
        Course, 
        verbose_name="Curso",
        related_name="enrollments",
        on_delete = models.PROTECT
    )

    status = models.IntegerField(
        'Situação', 
        choices=STATUS_CHOICES,
        default = 1,
        blank  = True
        )

    created_at = models.DateTimeField('Inscrito em ', auto_now_add=True)
    update_at = models.DateTimeField('Ultimo Status ', auto_now=True)   

    def active(self):
        self.status = 1 
        self.save()

    class Meta:
        verbose_name = "Inscrição"
        verbose_name_plural = "Inscrições"
        unique_together = (('user','course'))