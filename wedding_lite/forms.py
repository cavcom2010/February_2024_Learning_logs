from django import forms
from . models import RSVP

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['full_name', 'email_address', 'number_of_guests', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control-sm'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control-sm'}),
            'number_of_guests': forms.Select(attrs={'class': 'form-control-sm'}),
            'date_of_rsvp': forms.DateInput(attrs={'class': 'form-control-sm'}),
          'message': forms.Textarea(attrs={'class': 'form-control-sm'}),
        }








        # widgets = {
        #     'full_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'number_of_guests': forms.Select(attrs={'class': 'form-control'}),
        #  'message': forms.Textarea(attrs={'class': 'form-control'}),
