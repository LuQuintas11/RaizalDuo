from django.contrib import admin
from .models import Post, Comment, Show, Video, Lucia
from django_summernote.admin import SummernoteModelAdmin
from embed_video.admin import AdminVideoMixin





@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']

admin.site.register(Lucia)

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)




class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):   
    pass
admin.site.register(Video, MyModelAdmin)
