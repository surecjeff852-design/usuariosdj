from django.contrib import admin
from .models import Posts
# Register your models here.
admin.site.register(Posts)

class PostsAdmin(admin.ModelAdmin):
    list_display =(
        'ID',
        'post_type',
        'post_status',
        'post_title',
    )
    #
    def names (self, obj):
        #toda la operacion 
        print(obj.post_title)
        return obj.post_title 
    

    search_fields = ('post_title',)
