from django import forms


class NoteEditForm(forms.Form):
    note_text = forms.CharField(max_length=500)
    note_notify_start = forms.DateTimeField(initial=None, required=False)
    note_notify_gap = forms.DurationField(initial=None, required=False)
    checkbox_notify_start = forms.BooleanField(required=False)
    checkbox_notify_gap = forms.BooleanField(required=False)

class NoteAddForm(forms.Form):
    note_text = forms.CharField(max_length=500, required=True)
    author = forms.CharField(max_length=500, required=False)
    note_create_date = forms.DateTimeField(initial=None, required=False)
    note_notify_start = forms.DateTimeField(initial=None, required=False)
    note_notify_gap = forms.DurationField(initial=None, required=False)
