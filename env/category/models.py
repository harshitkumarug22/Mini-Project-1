from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200)
    description=models.TextField(max_length=300, blank=True)#as the description is optional
    image=models.ImageField(upload_to='photos/categories',blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def get_slug(self):
        return reverse('products_by_category', args=[self.slug])



    def __str__(self):
        return self.name