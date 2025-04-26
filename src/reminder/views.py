from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from reminder.forms import NoteForm
from reminder.instruments import convert_duration_to_time, convert_time_to_duration
from reminder.models import Note


@login_required
def note_add(request):
    form = NoteForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            note = Note()

            note.author = request.user
            note.note_text = form.cleaned_data.get('note_text')
            note.note_notify_start = form.cleaned_data.get('note_notify_start')
            note.note_notify_gap = form.cleaned_data.get('note_notify_gap')

            note.save()
            messages.success(request, 'Напоминание успешно создано!')
            return redirect('/reminder')
        else:
            print(1)

    return render(request, 'reminder/note_add.html', {'form': form})



@login_required
def notes_list(request):
    list_notes = Note.objects.filter(author=request.user)
    output = {"latest_note_list": list_notes}
    return render(request, 'reminder/notes_list.html', output)

@login_required
def note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    if request.user != note.author:
        return redirect('/reminder/login')

    if request.method == 'GET':
        note_notify_start_formated = timezone.localtime(note.note_notify_start).strftime("%Y-%m-%dT%H:%M") if note.note_notify_start else ''
        note_notify_gap_formated = convert_duration_to_time(note.note_notify_gap) if note.note_notify_gap else ''

        form = NoteForm(initial={
            'note_text': note.note_text,
            'note_notify_start': note_notify_start_formated,
            'note_notify_gap': note_notify_gap_formated
        })

    if (request.method == 'POST') and request.POST.get('edit_notify'):
        form = NoteForm(request.POST)
        if form.is_valid():
            note.note_text = form.cleaned_data.get('note_text')

            if form.cleaned_data.get('checkbox_notify_start'):
                form.cleaned_data.get('note_notify_start')
                note.note_notify_start = None
            elif form.cleaned_data.get('note_notify_start'):
                note.note_notify_start = form.cleaned_data.get('note_notify_start')

            if form.cleaned_data.get('checkbox_notify_gap'):
                form.cleaned_data.get('note_notify_gap')
                note.note_notify_gap = None
            elif form.cleaned_data.get('note_notify_gap'):
                note.note_notify_gap = convert_time_to_duration(form.cleaned_data.get('note_notify_gap'))
            note.save()
            return HttpResponseRedirect(reverse('reminder:note', args=(note_id,)))

    if (request.method == 'POST') and request.POST.get('del_notify'):
        note.delete()
        return redirect('/reminder/')

    return render(request, "reminder/note.html", {'note': note,
                                                  'form': form})


