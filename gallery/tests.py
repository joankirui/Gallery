from django.test import TestCase
from .models import Category,Image,Location

# Create your tests here.
class ImageTestClass(TestCase):
    # Set Up method
    def setUp(self):
        self.location = Location(location = 'Kericho')
        self.location.save_location()

        self.category = Category(category ='home')
        self.category.save_category()

        self.imaget = Image(id = 1,image_name = 'image1',image_description = 'this is the first image', image_location = self.location,category = self.category)
    def test_instance(self):
        self.assertTrue(isinstance(self.imaget,Image))

    def test_save_image(self):
        self.imaget.save_image()
        imagel = Image.objects.all()
        self.assertTrue(len(imagel) > 0)

    def test_delete_image(self):
        self.imaget.delete_image()
        imaged = Image.objects.all()
        self.assertTrue(len(imaged) == 0)