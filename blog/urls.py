from django.urls import path
from . import views

app_name = 'blog'

urlpatterns =[
	path('', views.index, name = 'index'),
	path('<int:year>/<int:month>/<int:day>/<slug:post>',\
	 		views.post_detail, name ='post-detail'),
	path('personal_detail', views.profile_detail, name = 'profile'),	
	path('event-manager', views.event_list, name="event-list")
]