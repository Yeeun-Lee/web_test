from django import forms

class FileForm(forms.Form):
    title = forms.CharField(max_length = 100)
    csvfile = forms.FileField(
        label = 'Select a file',
        help_text='only csv file(ex/prediction'
    )