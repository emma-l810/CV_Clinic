from django import forms
from .models import Address

# Create your forms here
class Form(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
