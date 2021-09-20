from django.contrib import admin
from .models import Category, Author, Post, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('category',)
    search_fields = ('category',)
    #list_editable = ('category',)


admin.site.register(Category, CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'surname', 'email', 'is_notified',)
    list_display_links = ('surname',)
    search_fields = ('first_name', 'surname', 'email',)
    list_editable = ('is_notified',)


admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pub_date', 'category',
        'headline', 'post_text', 'author'
    )
    list_display_links = ('headline',)
    search_fields = ('id', 'category', 'headline', 'author',)
    list_editable = ('author',)

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pub_date', 'post', 'comment_text',
    )
    list_display_links = ('comment_text',)
    search_fields = ('id', 'post', 'comment_text')
    #list_editable = ('post',)

admin.site.register(Comment, CommentAdmin)
