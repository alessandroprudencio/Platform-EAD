from django.db import models
from django.conf import settings
from taggit.managers import TaggableManager

class Thread(models.Model):

    title = models.CharField('Titulo', max_length=100)
    body = models.TextField('Mensagem')
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

    def get_absolute_url(self):
        return "duvida/%s" %(self.pk)


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
    correct = models.BooleanField('Correta?', blank=True, default=False)

    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em ', auto_now=True)

    def  __str__(self):
        return self.reply[:100]

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = "Respostas"
        ordering = ['-correct','created_at']

def post_save_repĺy(created, instance, **kwargs):
        instance.thread.answers =instance.thread.replies.count()
        instance.thread.save()

def post_delete_reply(instance,**kwargs):
        instance.thread.answers =instance.thread.replies.count()
        instance.thread.save()
        if instance.correct:
            instance.thread.replies.exclude(pk=instance.pk).update(
                correct=False
            )
    
models.signals.post_save.connect (
    post_save_repĺy, sender=Reply, dispatch_uid='post_save_repĺy'
)
models.signals.post_delete.connect (
    post_delete_reply, sender=Reply, dispatch_uid='post_delete_reply'
)