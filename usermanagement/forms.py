from django import forms
from usermanagement.models import User
from utils.models import OTP




class UserRegisterForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(max_length=255,min_length=8,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=255,min_length=8,widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    middle_name = forms.CharField(max_length=255,required=False)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("The provided email Aready exits in our system")
        return email
    
    def clean(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1!=password2:
            raise forms.ValidationError("The provided password did'nt match with each other ")
        return self.cleaned_data
    

    def save(self,commit=True):
        email = self.cleaned_data.get("email")
        password=self.cleaned_data.get("password2")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        middle_name = self.cleaned_data.get("middle_name")
        user = User(email=email,first_name=first_name,last_name=last_name,middle_name=middle_name)
        user.set_password(password)
        if commit:
            user.save()
        return user



class OtpVerificationForm(forms.Form):
    otp_code = forms.IntegerField()

    def clean_otp_code(self):
        otp = OTP.objects.filter(otp=self.cleaned_data.get("otp_code")).first()
        if not otp:
            raise forms.ValidationError("The provided OTP didn't match in our system ")
        return otp



class LoginUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
