from django import forms
from .models import Account, UserProfile


class RegistrationForms(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter Password",
                "class": "form-control",
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm Password",
                "class": "form-control",
            }
        )
    )

    class Meta:
        model = Account
        fields = {"first_name", "last_name", "email", "password"}

    def __init__(self, *args, **kwargs):
        super(RegistrationForms, self).__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs["placeholder"] = " Enter First Name"
        self.fields["last_name"].widget.attrs["placeholder"] = " Enter Last Name"
        self.fields["email"].widget.attrs["placeholder"] = " Enter Email"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {"addres", "profile_picture", "city", "state", "country"}
