
from django import forms
from .models import Tovar, Zakaz


class TovarForm(forms.ModelForm):
    class Meta: 
        model = Tovar
        execlude = ["id"]
        
        widgets = {
            "nazvanie": forms.TextInput(attrs={"class" : "form-input"})
        }

class ZakazForm(forms.ModelForm):
    class Meta: 
        model = Zakaz
        fields = ["tovar", "stauts", "punktVidachi"]

class FilterForm(forms.Form):
    q = forms.CharField(required=False, lable ="Поиск по названию")
    sort = forms.ChoiceField(required=False, choices =[
        {
            "nazanie": "По названию"
        }
    ])