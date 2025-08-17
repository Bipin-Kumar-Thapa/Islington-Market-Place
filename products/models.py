from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    stock = models.IntegerField(default=1)
    status = models.BooleanField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    product_image = models.ImageField(upload_to='photos/products/',blank=True)

    def clean(self):
        if self.discount_price and self.discount_price >= self.price:
            raise ValidationError("Discount price must be less than the original price.")

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    # def get_url(self):
    #     return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.name