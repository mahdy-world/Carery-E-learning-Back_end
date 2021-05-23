from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):

    username = forms.EmailField(max_length=30 , label='اسم المستخدم ')
    email = forms.EmailField(max_length=200, label = 'البريد الالكتروني')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}) , label='كلمة المرور' , )
    password2 = forms.CharField(widget=forms.PasswordInput , label='تأكيد كلمة المرور')

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['username','first_name','last_name','email'] 