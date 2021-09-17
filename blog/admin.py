from django.contrib import admin
from .models import Category, Author, Post, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_display_links = ('id',)
    search_fields = ('id', 'category')
    list_editable = ('category',)


admin.site.register(Category, CategoryAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'surname', 'email', 'is_notified')
    list_display_links = ('id',)
    search_fields = ('id', 'first_name', 'surname', 'email')
    list_editable = ('first_name', 'surname', 'is_notified')


admin.site.register(Author, AuthorAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pub_date', 'category',
        'headline', 'post_text', 'author'
    )
    list_display_links = ('id',)
    search_fields = ('id', 'category', 'headline', 'author')
    list_editable = ('headline', 'post_text', 'author')

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pub_date', 'post', 'comment_text',
    )
    list_display_links = ('id',)
    search_fields = ('id', 'post', 'comment_text')
    list_editable = ('post', 'comment_text')

admin.site.register(Comment, CommentAdmin)
