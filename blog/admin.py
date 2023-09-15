from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    # populate_fields slug to title
    # prepopulated_fields = {'slug': ('title',)}
    prepopulated_fields = {'slug': ['title', ]}


admin.site.register(Post, PostAdmin)
