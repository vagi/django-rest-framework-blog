# To start this script in CLI use command: $ python manage.py generate_posts -l=10

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker

from blog.models import Post, Author, Category

class Command(BaseCommand):

    # Description of the command will be placed in parameter 'help'
    help = 'Add new post(s) to the blog'

    # We parse all arguments in this method
    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=5)

    # We put a logic of the command here:
    def handle(self, *args, **options):
        #fake = Faker(['en-US', 'en_US', 'en_US', 'en-US'])
        fake = Faker()
        Faker.seed(0)

        # We use self.stdout.write instead of print to make visual inference of the process
        self.stdout.write('Generating of Posts has been started')
        for _ in range(options['len']):
            self.stdout.write('Generating Post {}'.format(_ + 1))
            # As per our model Post, it accepts author and category as corresponding
            # instances (Author and Category ... because of relationship (ForeignKey)
            # so we can not pass to the Post just a string
            author = Author.objects.filter(pk=1)
            # If there is no any author we ill create the one
            if not author:
                author = Author(
                    first_name='John',
                    surname = 'Dow',
                    email = 'john@dow.com',
                    is_notified = False,
                )
                author.save()
                author = Author.objects.filter(pk=1)

            # We can repeat the code as above to create fake category in case there is no any
            category = Category.objects.filter(pk=1)

            post = Post(category=category[0], author=author[0])
            # Faker generates text for new posts.
            # We may also give a list of designed texts to the Faker as parameter
            post.headline = fake.sentence(nb_words=8).upper()
            post.post_text = fake.paragraphs(nb=5)
            post.pub_date = timezone.now()
            # fake.word(ext_word_list=['Science', 'Heath', 'Life', 'Politics'])
            # fake.name(ext_word_list=['Peter Thiel', 'Steve Jobs', 'Bill Gates'])
            post.save()

        self.stdout.write('End generating Questions')
