from django import forms

class AlmacenForm(forms.Form):
     nombre = forms.CharField(max_length=50, required=True)
     precio = forms.DecimalField(max_digits=10, decimal_places=2,required=True)
     unidad = forms.DecimalField(max_digits=10, decimal_places=2,required=True)

class BebidaForm(forms.Form):
     nombre = forms.CharField(max_length=50, required=True)
     precio = forms.DecimalField(max_digits=10, decimal_places=2,required=True)
     unidad = forms.DecimalField(max_digits=10, decimal_places=2,required=True)

class VerduraForm(forms.Form):
     nombre = forms.CharField(max_length=50, required=True)
     precio = forms.DecimalField(max_digits=10, decimal_places=2,required=True)
     unidad = forms.DecimalField(max_digits=10, decimal_places=2,required=True)

class FrutaForm(forms.Form):
     nombre = forms.CharField(max_length=50, required=True)
     precio = forms.DecimalField(max_digits=10, decimal_places=2,required=True)
     unidad = forms.DecimalField(max_digits=10, decimal_places=2,required=True)