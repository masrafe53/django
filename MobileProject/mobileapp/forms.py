from django import forms
from django.db.models import fields
from mobileapp.models import mobile_model
from django.core.exceptions import ValidationError



class Mobile_modelForm(forms.ModelForm):
    class Meta():
        model = mobile_model
        fields = ('Brand_Name','Model','Color','JAN_Code','Image')
        
        
        def clean_Model(self):
            Model =self.cleaned_data['Model']
            if mobile_model.objects.filter(Model__iexact=Model).exists():
                raise forms.ValidationError("Alreay have")
            return Model
   

       
   
                