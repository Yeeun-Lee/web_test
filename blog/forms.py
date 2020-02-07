from .models import Submission

# class FileForm(forms.Form):
#     class Meta:
#         model = Submission
#         fields = ('submission_file')
#     def __init__(self, *args, **kwargs):
#         super(FileForm, self).__init__(*args, **kwargs)
#         self.fields['submission_file'].required = False