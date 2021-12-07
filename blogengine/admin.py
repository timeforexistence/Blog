from django.contrib import admin
from blogengine.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'upd_date', 'author', 'is_published', ) # 'tag'
    list_editable = ('is_published',)

    #def get_tags(self, obj):
    #    print("\n".join([t.title for t in obj.tag.all()]))


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)