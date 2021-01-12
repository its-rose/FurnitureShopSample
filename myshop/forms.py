from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    to_email = ['seitakhunova@gmail.com']