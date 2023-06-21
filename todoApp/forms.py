from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Todo

INPUT_CLASSES = 'w-full py-2 px-2 rounded border'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'username': 'Your Username',
        'class': INPUT_CLASSES,
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': INPUT_CLASSES
    }))
    
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'username': 'Your Username',
        'class': INPUT_CLASSES,
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your Email',
        'class': INPUT_CLASSES,
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': INPUT_CLASSES
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Retype Your Password',
        'class': INPUT_CLASSES
    }))        


class NewTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs= {'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs= {'class': INPUT_CLASSES})
        }
                
class EditTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': INPUT_CLASSES})
        }