from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=100)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, \
                                     null=True, blank=True)
    slug = models.SlugField(unique=True)  # Here Slug is the same as the title filed in django
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    @property
    def get_absolute_url(self):
        return reverse("product_detail_view", kwargs={
            "slug": self.slug
        })


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title

    @property
    def imageurl(self):
        return self.image.url
