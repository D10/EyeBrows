from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class SendMailForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'autocomplete': 'off'}))
    mail = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'autocomplete': 'off'}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    password = forms.CharField(max_length=150, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=150, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=150, label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=150, label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
