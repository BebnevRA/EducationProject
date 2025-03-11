from django import forms


class NoteForm(forms.Form):
    note_text = forms.CharField(max_length=500)
    author = forms.CharField(max_length=500, required=False)
    note_notify_start = forms.DateTimeField(initial=None, required=False)
    note_notify_gap = forms.DurationField(initial=None, required=False)
    checkbox_notify_start = forms.BooleanField(required=False)
    checkbox_notify_gap = forms.BooleanField(required=False)

    def clean_note_notify_gap(self):
        note_notify_gap = self.cleaned_data['note_notify_gap']
        note_notify_start = self.cleaned_data['note_notify_start']
        if note_notify_gap and (note_notify_start is None):
            raise forms.ValidationError('Для создания промежутка - задайте время первого уведомления')
        return note_notify_gap