import os

from django.forms.fields import CharField, ImageField, FileInput, IntegerField
from django.forms.widgets import TextInput, NumberInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.exceptions import ValidationError

from authapp.models import User
from authapp.validator import validate_name


class UserLoginForm(AuthenticationForm):
    # username = CharField(widget=TextInput(), validators=[validate_name])

    class Meta :
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs) :
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items() :
            field.widget.attrs['class'] = 'form-control py-4'


class UserRegisterForm(UserCreationForm):

    class Meta :
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs) :
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл.почты'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        for field_name, field in self.fields.items() :
            field.widget.attrs['class'] = 'form-control py-4'

    # def clean_username(self):
    #     data = self.cleaned_data['username']
    #     if len(data) < 3:
    #         raise ValidationError('Короткое имя пользователя')
    #     return data


class UserProfileForm(UserChangeForm):

    image = ImageField(widget=FileInput(), required=False)
    age = IntegerField(widget=NumberInput(), required=False)

    class Meta :
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'image', 'age')

    def __init__(self, *args, **kwargs) :
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True

        for field_name, field in self.fields.items() :
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

    # def clean_image(self) :
    #     data = self.cleaned_data['image']
    #     if data.size > 20000 :
    #         raise ValidationError('Слишком большой размер файла')
    #     return data
    #
    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if len(data) < 3:
    #         raise ValidationError('Короткое имя пользователя')
    #     return data
