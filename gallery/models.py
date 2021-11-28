from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_location(cls):
        place = cls.objects.all()
        return place

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()

class Image(models.Model):
    # image = models.ImageField()
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_image(cls,search_term):
        images = cls.objects.filter(category__category__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls,location):
        img_location = Image.objects.filter(location = location).all()
        return img_location
        
    class Meta:
        ordering = ['image_name']

  