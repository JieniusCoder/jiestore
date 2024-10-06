from django.db import models
import datetime


# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    video_url = models.CharField(max_length=500, default='', blank=True)
    is_paid = models.BooleanField(default=False)

    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    def create_product(self, name, price, image, category, video_url):
        product = Products(name=name, price=price, image=image, category=category, video_url=video_url)
        product.save()
        return product
    
    def update_product(self, id, **kwargs):
        product = Products.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(product, key, value)
        product.save()
        return product
    
    def delete_product(self, id):
        product = Products.objects.get(id=id)
        product.delete()
        return product
    

class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def create_category(self, name):
        category = Category(name=name)
        category.save()
        return category
    
    def update_category(self, id, **kwargs):
        category = Category.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(category, key, value)
        category.save()
        return category
    
    def delete_category(self, id):
        category = Category.objects.get(id=id)
        category.delete()
        return category
    

