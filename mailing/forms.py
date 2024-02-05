from django import forms
from mailing.models import Mailing


class MailingForm(forms.ModelForm):
    """
    This form for creating and updating mailing.
    """

    class Meta:
        model = Mailing
        exclude = ('user', 'status',)
        #widgets = {'data_mailing': forms.DateTimeInput(attrs={'type': 'date'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_data_mailing_finish(self):
        if self.cleaned_data.get('data_mailing_finish'):
            data_mailing = self.cleaned_data.get('data_mailing')
            data_mailing_finish = self.cleaned_data.get('data_mailing_finish')
            if data_mailing_finish > data_mailing:
                return data_mailing_finish
            else:
                raise forms.ValidationError('Finish date of mailing should be after begin date')
