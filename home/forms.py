from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models

class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('photo', 'username', 'first_name', 'last_name', 'email', 'phone', 'city', 'country', 'gender', 'date_of_birth')
        widgets = {
            'username': forms.TextInput(attrs={
                "class" : "b-none border-ccc p-10 mt-3 rad-6 d-block w-full",
                "type":"text",
                "id":"first",
                'placeholder': 'User Name'
                }
                ),
            'city': forms.TextInput(attrs={
                "class" : "b-none border-ccc p-10 mt-3 rad-6 d-block w-full",
                "type":"text",
                "id":"first",
                'placeholder': 'City'
                }
                ),
            'country': forms.TextInput(attrs={
                "class" : "b-none border-ccc p-10 mt-3 rad-6 d-block w-full",
                "type":"text",
                "id":"first",
                'placeholder': 'Country'
                }
                ),
            'first_name': forms.TextInput(attrs={
                "class" : "b-none border-ccc p-10 mt-3 rad-6 d-block w-full",
                "type":"text",
                "id":"first",
                'placeholder': 'First Name'
                }
                ),
            'last_name': forms.TextInput(attrs={
                "class" : "b-none border-ccc p-10 rad-6 d-block w-full",
                "type":"text",
                "id":"first",
                'placeholder': 'Last Name'
                }
                ),
            
            'email': forms.TextInput(attrs={
                "class":"b-none border-ccc p-10 mt-3 rad-6 w-full mr-10",
                "id":"email",
                "type":"email"
            }),
            'phone': forms.TextInput(attrs={
                "class":"b-none border-ccc p-10 rad-6 w-full mr-10",
                "id":"number",
                "placeholder":"Phone Number"
                }
                ),
            'date_of_birth': forms.DateInput(attrs={
                "class":"b-none border-ccc p-10 rad-6 d-block w-full",
                "id":"date",
                "type":"date"
            }
            ),
            'gender': forms.Select(attrs={
                "id":"gender",
                "class":"form-select form-select-lg mb-3 d-block w-100"
            }
            ),
            'photo': forms.TextInput(attrs={
                'class':"b-none border-ccc p-10 rad-6 d-block w-full",
                'type':"file",
                'id':"pic"
                }
                ),


        }

class SignUpForm(UserCreationForm):
    class Meta:
        model=models.User
        fields=('username','email','password1','password2', 'phone')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Password (again)'})


class CustomerMessageForm(forms.ModelForm):
    class Meta:
        model = models.CustomerMessage
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', "rows":"5"})
        }
        fields = '__all__'
