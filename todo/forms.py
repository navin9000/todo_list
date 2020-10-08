from django import forms
from .models import todomodel

class todoform(forms.ModelForm):
	class Meta():
		model = todomodel
		fields = '__all__'
		widgets = {
		    'todo' : forms.Textarea(attrs={'class':'textarea',"rows":3,"cols":100,'placeholder':'todo'})
		}
