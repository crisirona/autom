from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Demanda


class DemandaForm(forms.ModelForm):

    class Meta:
        model = Demanda
        fields = ('id_demanda','fecha','hora','tipodemanda','detalle',
                    'rut1','dv1','nombre1','apellido1','telefono1','comuna1',
                    'rut2','dv2','nombre2','apellido2','telefono2','comuna2')


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class Registro(UserCreationForm):
    pass

class CustomUserCreationForm(UserCreationForm):  
    class Meta:
        model = User
        fields = ['last_name','username','email','password1','password2']
    
  