from django.test import TestCase
from . models import Profile,Project,Ratings

# Create your tests here.
class ProfileTest(TestCase):

    def setUp(self):
        self.profile = Profile(name = 'John', profile_photo = 'image.jpg', bio = 'A bio', number = '0758845666', email = 'paulmburu08@gmail.com', address = 'Karen', creat_date= '2019-08-08')

    def tearDown(self):
        Profile.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

class ProjectTest(TestCase):

    def setUp(self):
        self.project = Project(title = 'Project', landing_page_image = 'image.jpg', description = 'A test', link = 'www.gmail.com', technologies = 'HTML', collaborators = 'Karen', post_date= '2019-08-08')

    def tearDown(self):
        Project.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

class RatingsTest(TestCase):

    def setUp(self):
        self.ratings = Ratings(design = 2, usability = 3, content = 4, average = 5)

    def tearDown(self):
        Ratings.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ratings,Ratings))