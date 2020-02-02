from django.contrib import admin
from .models import Post, Notice, Submission
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')

class SubmitAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_ranking')
    list_filter = ('user_ranking',)
    search_fields = ('user_name', 'submission_file')

admin.site.register(Post, PostAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Submission, SubmitAdmin)