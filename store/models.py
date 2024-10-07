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
    # if is_paid is True, the video url is unlocked
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
    
    def set_is_paid(self, id):
        product = Products.objects.get(id=id)
        product.is_paid = True
        product.save()
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
    

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return None
    
    def register(self, first_name, last_name, email, password):
        customer = Customer(first_name=first_name, last_name=last_name, email=email, password=password)
        customer.save()
        return customer
    
    def update_customer(self, id, **kwargs):
        customer = Customer.objects.get(id=id)
        for key, value in kwargs.items():
            setattr(customer, key, value)
        customer.save()
        return customer
    
    def delete_customer(self, id):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return customer
    
    
class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def get_orders_by_customer(self, customer):
        return Order.objects.filter(customer=customer)
    
    def create_order(self, product, customer):
        order = Order(product=product, customer=customer)
        order.save()
        return order


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=500)
    payment_status = models.CharField(max_length=500)
    payment_time = models.DateTimeField(default=datetime.datetime.now())
    
    def create_payment(self, order, payment_id, payment_status):
        payment = payment(order=order, payment_id=payment_id, payment_status=payment_status)
        payment.save()
        return payment
    
    def delete_payment(self, id):
        payment = payment.objects.get(id=id)
        payment.delete()
        return payment
    
    def change_payment_status(self, id, payment_status):
        payment = payment.objects.get(id=id)
        payment.payment_status = payment_status
        payment.save()
        return payment