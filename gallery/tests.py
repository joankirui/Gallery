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

    def test_get_image_by_id(self):
        found_image = self.imaget.get_image_by_id(self.imaget.id)
        image = Image.objects.filter(id=self.imaget.id)
        self.assertFalse(found_image,image)

    def test_search_image(self):
        category = 'home'
        found_img = self.imaget.search_image(category)
        self.assertFalse(len(found_img) > 1)

    def test_filter_by_location(self):
        self.imaget.save_image()
        found_images = self.imaget.filter_by_location(location = 'Kericho')
        self.assertTrue(len(found_images) == 1)


class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(location = 'Kericho')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        locationss = Location.objects.all()
        self.assertTrue(locationss(len) == 0)



class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(category='home')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)