from django import forms
from Gym.models import Bebida, Entrenador, Clase

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = '__all__'

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = '__all__'
        
class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'