from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.
class Products(models.Model):
    productName=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    description=models.TextField(max_length=600, blank=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    model_category=models.ForeignKey(Category, on_delete=models.CASCADE)
    date_creation=models.DateTimeField(auto_now_add=True)
    modified_creation=models.DateTimeField(auto_now_add=True)

    def get_slug(self):
        return reverse('productInfo', args=[self.model_category.slug,self.slug])

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return self.productName