import datetime
from django import forms
from django.contrib.auth import get_user_model
from users.context_processors import get_content_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm


class AddPostForm(forms.ModelForm):
    class Meta:
        model = get_content_model()
        fields = ['header_ru', 'header_en', 'post_ru', 'post_en', 'category', 'author', 'photo', 'slug', 'is_published']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Login: '), widget=forms.TextInput())
    password = forms.CharField(label=_('Password: '), widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label=_('Login: '), widget=forms.TextInput())
    email = forms.CharField(label=_('E-mail: '), widget=forms.EmailInput())
    password1 = forms.CharField(label=_('Password: '), widget=forms.PasswordInput())
    password2 = forms.CharField(label=_('Password retry: '), widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(_('This E-mail already exists!'))
        return email


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(label=_('Change login: '), widget=forms.TextInput())
    email = forms.CharField(label=_('Change E-mail: '), widget=forms.EmailInput())
    this_year = datetime.date.today().year
    date_birth = forms.DateField(widget=forms.SelectDateWidget(years=tuple(range(this_year - 150, this_year - 5))))

    class Meta:
        model = get_user_model()
        fields = ['photo', 'username', 'email', 'date_birth', 'first_name', 'last_name']


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Current password'), widget=forms.PasswordInput())
    new_password1 = forms.CharField(label=_('New password'), widget=forms.PasswordInput())
    new_password2 = forms.CharField(label=_('Confirm password'), widget=forms.PasswordInput())
