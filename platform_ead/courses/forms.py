from django import forms

from django.core.mail import send_mail
from django.conf import settings

from platform_ead.core.mails import send_email_template

class ContactCourse(forms.Form):

    name = forms.CharField(label="Seu nome")
    email = forms.EmailField(label="E-mail")
    message = forms.CharField(label="Mensagem/Duvida", widget = forms.Textarea)


    def send_mail(self, course):
        subject = 'Contato sobre o curso:  %s' % course
        context = {
            'name':self.cleaned_data['name'],
            'email':self.cleaned_data['email'],
            'message':self.cleaned_data['message']
        }

        template_name = 'pages/contact_email.html'

        send_email_template(subject, template_name,  context ,[settings.CONTACT_EMAIL])
