from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class QrForm(forms.Form):
    
    restaurant = forms.CharField(max_length=40, 
                                 label='Restaurant Name',
                                 widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'placeholder':'Enter URL name'
                                })
                                
                                
                                 )
    url = forms.URLField(max_length=200, required=False, label='Menu URL',
                         widget=forms.URLInput(attrs={
                             'class':'form-control',
                             'placeholder':'Enter your URL of Menu'
                         }))
    file = forms.FileField(required=False, label="Upload File (PDF, Excel, CSV)",
                           widget=forms.FileInput(attrs={
                               'class':'form-control',
                               'placeholder':'Upload your file'
                           })
                           
                           
                           )
    
  #Registration form  

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')
        
        
    

    help_texts = {
        'username': None,
        'password1': None,
        'password2': None
    }
    
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     url = cleaned_data.get('url')
    #     file = cleaned_data.get('file')
        
    #     if not url  and not file:
    #         raise forms.ValidationError('Please provide either a URL or Upload a file')
        
    #     return cleaned_data