from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    # we want to use summer note for our content django text field
    prepopulated_fields = {'slug': ('title',)}
    # add a filter to admin page to search by satus
    # (draft/posted) or when created
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')

# admin.site.register(Post) - this method
# only allows 2 arguments to be passed to it
# so I have added the @admin decorator aove the PostAdmin class


@admin.register(Comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
