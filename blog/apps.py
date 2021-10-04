from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    # Signal receivers are connected in the ready() method of your application
    # configuration class. If you’re using the receiver() decorator, import the
    # signals submodule inside ready().
    def ready(self):
        import blog.signals
