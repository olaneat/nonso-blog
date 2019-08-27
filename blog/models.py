from django.utils import timezone
from django.db import models
from django.urls import reverse
from .constant import publish_choices
# Create your models here.

class Author(models.Model):
	full_name = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.full_name


class Post(models.Model):
	title = models.CharField(max_length = 200)
	slug = models.SlugField(max_length = 200, unique_for_date = 'published')
	author = models.ForeignKey(Author, on_delete = models.CASCADE)
	news = models.TextField()
	status = models.CharField(max_length = 5, choices = publish_choices)
	created = models.DateField(default = timezone.now)
	published = models.DateField()
	

	def get_absolute_url(self):
		return reverse('blog:post-detail', args = [self.published.year,
											self.published.month,
											self.published.day,
											self.slug])

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = ('Posts')
		verbose_name_plural = ('Post')
		ordering = ('-created',)

class Comment(models.Model):
	name = models.CharField(max_length = 150)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateField(auto_now=True)
	post = models.ForeignKey(Post, on_delete = models.CASCADE,
							  related_name='comments')
	active = models.BooleanField(default=True)
	class Meta:
		ordering = ('-created',)
	
	def __str__(self):
		return 'comment by {}, on {}'.format(self.name, self.post)



class Job(models.Model): 
	developer_name = models.ForeignKey('Profile', on_delete=models.CASCADE)
	project_name = models.CharField(max_length = 200)
	created = models.DateField()
	stagging_environment = models.CharField(max_length = 150)
	role = models.CharField(max_length = 200)
	project_detail = models.TextField()
	technologies_used = models.TextField()
	published = models.DateTimeField()

	def __str__(self):
		return self.project_name

	def get_absolute_url(self):
		return reverse('blog:project-detail', args = [self.id, self.project_name])

	class Meta:
		ordering = ['-published']

class Qualification(models.Model):
	user = models.ForeignKey('Profile', on_delete = models.CASCADE)
	qualification_one = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	date = models.DateField()
	published = models.DateTimeField()

	def __str__(self):
		return self.name

	def get_absolute_url():
		return reverse('blog:qualification-detail', args = [self.id, self.name])
	class Meta:
		ordering = ['-published']

class Profile(models.Model):
	name = models.CharField(max_length = 100)
	slug = models.SlugField(max_length = 100)
	email = models.EmailField()
	nationality = models.CharField(max_length = 100)
	address = models.CharField(max_length = 200)
	phone_number = models.CharField(max_length = 15)
	aim = models.TextField()
	languages = models.TextField()
	frameworks = models.TextField()
	hardware = models.TextField()
	skills = models.TextField()
	picture = models.ImageField(upload_to = 'media/img')
	project_one_name = models.CharField(max_length = 200)
	created_one = models.DateField()
	stagging_one_environment = models.CharField(max_length = 150)
	role_one = models.CharField(max_length = 200)
	project_one_detail = models.TextField()
	technology_one_used = models.TextField()
	project_two_name = models.CharField(max_length = 200)
	created_two = models.DateField()
	stagging_two_environment = models.CharField(max_length = 150)
	role_two = models.CharField(max_length = 200)
	project_two_detail = models.TextField()
	technology_two_used = models.TextField()
	project_three_name = models.CharField(max_length = 200)
	created_three = models.DateField()
	stagging_three_environment = models.CharField(max_length = 150)
	role_three = models.CharField(max_length = 200)
	project_three_detail = models.TextField()
	technology_three_used = models.TextField()
	qualification_one = models.CharField(max_length = 100)
	location_one = models.CharField(max_length = 100)
	date_one = models.DateField()
	qualification_two = models.CharField(max_length = 100)
	location_two = models.CharField(max_length = 100)
	date_two = models.DateField()
	qualification_three = models.CharField(max_length = 100)
	location_three = models.CharField(max_length = 100)
	date_three = models.DateField()
	qualification_four = models.CharField(max_length = 100)
	location_four = models.CharField(max_length = 100)
	date_four = models.DateField()
	qualification_five = models.CharField(max_length = 100)
	location_five = models.CharField(max_length = 100)
	date_five = models.DateField()
				

	def __str__(self):
		return self.name

	
class Event(models.Model):
    user = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length=100)
    detail = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    class Meta:
    	ordering = ('-start_date',)

    def __str__(self):
    	return 'event_title {}, by user{}'.format(self.event_title, self.user)

    def get_absolute_url(self):
    	return reverse("event-detail", args={"id": self.id,
												'slug': self.slug})
		
