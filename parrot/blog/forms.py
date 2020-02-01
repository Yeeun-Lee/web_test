from django import forms

class FileForm(forms.Form):
    csvfile = forms.FileField(
        label = 'Select a file',
        help_text='only csv file(ex/prediction'
    )