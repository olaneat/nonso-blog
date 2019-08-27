from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Profile, Event
from .forms import CommentForm, EventForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.views import generic
from flatpickr.utils import GenericViewWidgetMixin
# Create your views here.

def index(request):
	news = Post.objects.all()
	paginator = Paginator(news, 1)
	page = request.GET.get('page')
	try:
		post = paginator.page(page)
	except PageNotAnInteger:
		post =paginator.page(1)
	except EmptyPage:
		post = paginator.page(paginator.num_pages)
	return render(request, 'blog/index.html', {'post':post, 'page': page})

def post_detail(request, post, year, month, day):
	post = get_object_or_404(Post,	published__year = year,
									published__month = month,
									published__day = day,
									slug = post)
	
	comments = post.comments.filter(active=True)
	comment_info = None
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			comment_info = comment_form.save(commit=False)
			comment_info.post=post
			comment_info.save()
	else:
		comment_form = CommentForm()

	context = {'post': post, 'comments':comments,
				'comment_info': comment_info, 'comment_form': comment_form}
	return render(request, 'blog/news-detail.html', context )
	


def profile_detail(request):
	profile = get_object_or_404(Profile)
	return render(request, 'blog/profile-detail.html', {'profile': profile})


'''class EventList(GenericViewWidgetMixin, generic.edit.CreateView):
	models = Event
	event_form = EventForm
	template_name = 'blog/event-list.html'
	fields = ['title', 'detail' 
				'start_date', 'end_date', 
				'start_time', 'end_time'
	]
	widgets = {
		'start_date': DatePickerInput().start_of('event day'),
		'end_date': DatePickerInput(). end_of('event day'),
		'start_time': TimePickerInput().start_of('event time'),
		'end_time': TimePickerInput().end_of('event time')
	}
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title_text'] = 'Generic View without using model form'
		context['submit_text'] = 'Create Event'
		return context


class EventUpdate(generic.edit.UpdateView):
	model = Event
	event_form = EventForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title_text'] = 'Generic View using model form'
		context['submit_text'] = 'Update Event'
		return context
'''

def event_list(request):
	events = Event.objects.all()
	if request.method == 'POST':
		event_form = EventForm()
		if event_form.is_valid():
			event_form.save()
	else:
		event_form = EventForm()
	context = {'events': events, 'event_form': event_form}
	return render(request, 'blog/event-list.html', context)


def event_detail(request, id, slug):
	event_details = get_object_or_404(Event, id = id,
											slug = slug)
	return render(request, 'blog/event-detail.html', {'event_details': event_details}) 