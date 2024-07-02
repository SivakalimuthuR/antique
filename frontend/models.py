from django.db import models

# class post(models.Model):
#     title = models.CharField(max_length=250)
#     content = models.TextField()
#     img_url = models.URLField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

# #optional

#     def __str__(self):
#         return self.title


class Product(models.Model):
    productname = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    starting_price = models.DecimalField(max_digits=20, decimal_places=2)
    closing_time = models.DateField()


    def __str__(self):
         return self.title