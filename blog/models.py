from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.EmailField()
    is_notified = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.surname)


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Post(models.Model):
    headline = models.CharField(max_length=200)
    post_text = models.TextField()
    pub_date = models.DateField('date_published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)   # Post has Many-To-One relationship with a Category
    author = models.ForeignKey(Author, on_delete=models.CASCADE)   # Post has Many-To-One relationship with an Author

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['pub_date']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)    # Comment has Many-To-One relationship with a Post
    comment_text = models.CharField(max_length=200)
    pub_date = models.DateField('date_commented')
    # protected = False

    def __str__(self):
        return self.comment_text

    # Customized delete method for Comment Model that would work with Signal pre_delete
    # def delete(self, *args, **kwargs):
    #     if self.protected is True:
    #         print("This commentary is protected")
    #         return
    #     else:
    #         super().delete(*args, **kwargs)  # Call the "real" delete() method.

