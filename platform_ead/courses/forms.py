from django import forms

class ContactCourse(forms.Form):

    name = forms.CharField(label="Seu nome")
    email = forms.EmailField(label="E-mail")
    message = forms.CharField(label="Mensagem/Duvida", widget = forms.Textarea)
