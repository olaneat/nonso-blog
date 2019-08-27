from django.contrib import admin
from .models import  Profile, Post, Author,  Job, Comment, Event

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'news', 'author', 'published' ]
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('title',)
	list_editable_link = ['title', 'news']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('full_name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['name']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'post']
    search_fields = ('name', )
    list_editable = ['active']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
	list_display = ('title', 'start_date', 'end_date')
	list_editable_link = ['title']
	list_editable = ('start_date', 'end_date')
	prepopulated_fields = {'slug': ('title',)}