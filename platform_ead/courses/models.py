from django.db import models

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
