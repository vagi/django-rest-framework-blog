from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker

from blog_project.blog.models import Post

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
        fake.seed(1)

        # We use self.stdout.write instead of print to make visual inference of the process
        self.stdout.write('Generating of Posts has been started')
        for _ in range(options['len']):
            self.stdout.write('Generating Post {}'.format(_ + 1))
            post = Post()
            # Faker generates text for the posts.
            # We may also give a list of designed questions to the Faker as parameter
            post.headline = fake.sentence(nb_words=8).upper()
            post.post_text = fake.paragraphs(nb=5)
            post.pub_date = timezone.now()
            post.category = fake.word(ext_word_list=['Science', 'Heath', 'Life', 'Politics'])
            post.author = fake.name(ext_word_list=['Peter Thiel', 'Steve Jobs', 'Bill Gates'])
            post.save()

        self.stdout.write('End generating Questions')
