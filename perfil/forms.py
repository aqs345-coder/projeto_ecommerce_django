from django import forms
from . import models
from django.contrib.auth.models import User


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)

# TODO: Esconder a senha durante a digitação
# TODO: Não permitir colagem no campo da senha


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Senha'
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label='Confirme a senha'
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'username', 'password', 'password2')

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data
        validation_error_msgs = {}
        usuario_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'Já existe um usuário com esse nome de usuário.'
        error_msg_email_exists = 'Já existe um usuário com esse email.'
        error_msg_passwords_different = 'As senhas não são iguais.'
        error_msg_password_short = 'A senha deve conter pelo menos 8 caracteres.'

        if self.usuario:
            if usuario_db:
                if usuario_data != usuario_db:
                    validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                if email_data != email_db:
                    validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_passwords_different

                if len(password_data) < 8:
                    validation_error_msgs['password'] = error_msg_password_short
        else:
            pass
        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))
