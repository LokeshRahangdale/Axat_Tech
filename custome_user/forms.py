from django import forms
from django.forms import fields
from .models import CustUser,student_model, teacher_model
from django.contrib.auth.forms import UserCreationForm
class Register_Form(UserCreationForm):
    mobile_num = forms.CharField(
        widget=forms.TextInput(
            attrs={ 
                "placeholder" : "Mobile Number",                
                "class": "form-control"
            }
        ))
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={ 
                "placeholder" :"Enter Name",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Confirm Password",                
                "class": "form-control"
            }
        ))
    class Meta:
        model = CustUser
        fields = ('email','name','password1','mobile_num',)

class ImgForm(forms.ModelForm):
    class Meta:
        model = student_model
        fields = ('student_image',)

class TeacherImgForm(forms.ModelForm):
    class Meta:
        model = teacher_model
        fields = ('image1','image2','image3')