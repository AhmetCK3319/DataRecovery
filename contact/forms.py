from django import forms
from django.core.mail import EmailMessage
from django.conf import settings


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Name & Surname"}
        ),
    )
    email = forms.EmailField(
        max_length=50,
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Email"}
        ),
    )
    phone = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Phone"}
        ),
    )
    message = forms.CharField(
        max_length=500,
        required=True,
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Message"}
        ),
    )

    def clean(self):
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        phone = self.cleaned_data.get("phone")
        message = self.cleaned_data.get("message")

        if name and email and phone and message:
            return self.cleaned_data
        else:
            raise forms.ValidationError("Please fill in the required fields.")

    def send_email(self):
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        phone = self.cleaned_data.get("phone")
        message = self.cleaned_data.get("message")

        mesaj_context = f"Name & Surname: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        email = EmailMessage(
            subject=f"Contact Form Submission from {name}",
            body=mesaj_context,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email],
        )
        email.send()

        # Clear the form data
        self.cleaned_data.clear()
