from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Your Name",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your full name',
        })
    )

    email = forms.EmailField(
        label="Your Email",
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email address',
        })
    )

    subject = forms.CharField(
        max_length=200,
        label="Subject",
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject of your message',
        })
    )

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            'placeholder': 'Type your message here...',
            'rows': 6
        })
    )
