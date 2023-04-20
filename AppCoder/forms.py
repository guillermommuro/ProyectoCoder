from django import forms

class cursocormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()