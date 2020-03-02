from django.test import TestCase
from django.test import TestCase
from .models import Image,Category,Location
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Location))
    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class CategoryTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_location = Location(name = 'testing')
        self.new_location.save()

        self.new_image= Image(title = 'Test Category',post = 'This is a random test Post',image = self.james)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

   def test_get_mygallery_today(self):
        today_mygallery = Article.todays_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_mygallery_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_mygallery(date)
        self.assertTrue(len(news_by_date) == 0)