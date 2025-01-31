from django import forms
from .models import Pessoa 
from django.contrib.auth.hashers import make_password

class PessoaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Pessoa
        fields = ['username', 'nome', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Pessoa.objects.filter(username=username).exists():
            raise forms.ValidationError("Este usuário já está em uso.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Pessoa.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email
    
    def save(self, commit=True):
        pessoa = super().save(commit=False)
        pessoa.password = make_password(self.cleaned_data['password'])
        if commit:
            pessoa.save()
        return pessoa