from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


# class ContactForm(forms.Form):
#     fullname = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Your full name"
#             }
#         )
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Your email"
#             }
#         )
#     )
#     content = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Your message"
#             }
#         )
#     )

#     # # If username matched existing user error will Rise
#     # def clean_username(self):
#     #     uname = self.cleaned_data.get('username')
#     #     if User.objects.filter(username=uname).exists():
#     #         raise forms.ValidationError(
#     #             "This username is already exists! try unique.")
#     #     return uname 
    
#     # # If gmail matched existing user error will Rise
#     # def clean_email(self):
#     #     email = self.cleaned_data.get("email")
#     #     if User.objects.filter(email=email).exists():
#     #         raise forms.ValidationError(
#     #             "Customer with this email already exists.")

#     #     return email

#     # If email not gmail.com error will Rise(example as gmail)
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if not 'gmail.com' in email:
#             raise forms.ValidationError('Email has to be gmail.com')
#         return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())



class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password" , widget=forms.PasswordInput())



    # If username matched existing user error will Rise
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError(
                "Username is already exists!")
        return username
    
    # If gmail matched existing user error will Rise
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError(
                "Email is already exists!")
        return email

    # # If email not gmail.com error will Rise(example as gmail)
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not 'gmail.com' in email:
    #         raise forms.ValidationError('Email has to be gmail.com')
    #     return email


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Password didn't match!")
        return data

