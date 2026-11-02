from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Name',
                'required': True,
                'id': 'contact-name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Email Address',
                'required': True,
                'id': 'contact-email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Subject / Project Inquiry',
                'required': True,
                'id': 'contact-subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-input form-textarea',
                'placeholder': 'Tell me about your project, timeline, or question...',
                'rows': 5,
                'required': True,
                'id': 'contact-message'
            }),
        }
