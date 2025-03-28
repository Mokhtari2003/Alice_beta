from django import forms
from .models import UserAccount
class UserAccountsForm(forms.ModelForm):
    password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'confirmPassword',
        'placeholder': 'Confirm Password' 
    }),
)
    class Meta:
        model = UserAccount
        fields = ["username" ,"email" ,"phone_number" ,"password"]    
        widgets = {
            'username':
                forms.TextInput(
                attrs={
                    'class': 'form-control' ,
                    'id': 'username'  ,
                    'placeholder': "Username"
                    }),
            'email':
                forms.EmailInput(
                    attrs={
                        'class': 'form-control' ,
                        'id': "signupEmail" ,
                        'placeholder': "Email"
                        }),
            'phone_number':
                forms.TextInput(
                    attrs={
                        'class': 'form-control' ,
                        'id': "phone" ,
                        'placeholder': "Phone Number"
                        }),
            'password':
                forms.PasswordInput(
                    attrs={
                        'class': 'form-control' ,
                        'id': "signupPassword" ,
                        'placeholder': "Password"
                        }),
            'password2':
                forms.PasswordInput(
                    attrs={
                        'class': 'form-control' ,
                        'id': "confirmPassword" ,
                        'placeholder': "Password Conform"
                        }),
            
            
        }    