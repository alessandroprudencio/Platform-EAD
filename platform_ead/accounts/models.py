from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

import re

from django.core import validators

from django.conf import settings

class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField('Nome Usuário', unique=True, max_length=50,
     validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
     'Nome de usuário só pode conter letras, digitos ou os seguintes caracteres:@/./+/-/_','invalid')]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome Completo', blank=True, max_length=150)
    photo_profile = models.ImageField(upload_to='courses/image', blank=True)
    is_active = models.BooleanField('Usuário Ativo ?', default=True)
    is_staff = models.BooleanField('È da equipe.?', default=False)
    date_joined = models.DateTimeField('Data Cadastro', auto_now_add=True)

    objects  = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = "Usuários"

class PasswordReset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário',on_delete = models. CASCADE,  related_name='resets')

    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateField("Criado em", auto_now_add=True)
    confirmed = models.BooleanField('Confirmado?', default=False, blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.user, self.created_at)

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas Senhas'
        ordering = ['-created_at']
    
