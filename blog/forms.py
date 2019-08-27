from django import forms
from .models import Comment, Event
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body',) 


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'detail',
            'start_date', 'end_date',
            'start_time', 'end_time',
        ]

        widgets = {
            'start_date':   DatePickerInput().start_of('event active days'),
            'end_date':     DatePickerInput().end_of('event active days'),
            'start_time':   TimePickerInput().start_of('event active time'),
            'end_time':     TimePickerInput().end_of('event active time'),
        }