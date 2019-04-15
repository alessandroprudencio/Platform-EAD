from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

class Thread(models.Model):

    title = models.CharField('Titulo', max_length=100)
    body = models.TextField(u'Mensagem')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Autor',
        on_delete = models.CASCADE,
        related_name="threads"
    )
    views = models.IntegerField('Visualizações', blank=True, default= 0)
    answers = models.IntegerField('Respostas',blank=True, default=0)
    tags = TaggableManager()

    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)


    def  __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = "Tópicos"
        ordering = ['-update_at']

class Reply(models.Model):

    thread = models.ForeignKey(
    Thread,
    verbose_name='Tópico',
    on_delete = models.CASCADE,
    related_name="replies"
    )

    reply = models.TextField('Resposta')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Autor',
        on_delete = models.CASCADE,
        related_name="replies"
    )
    views = models.IntegerField('Visualizações', blank=True, default= 0)
    answers = models.IntegerField('Respostas',blank=True, default=0)
    tags = TaggableManager()

    correct = models.BooleanField('Correta?', blank=True, default=False)

    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)

    def  __str__(self):
        return self.reply[:100]

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = "Respostas"
        ordering = ['-correct','created_at']
