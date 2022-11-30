from django.db import models

# Create your models here.

# class Cliente(models.Model):
#     name = models.CharField(max_length=15, help_text="Name")
#     lastName = models.CharField(max_length=20, help_text="Last Name")
#     email = models.EmailField(blank=True, null=True, help_text="Email Address")
#     password = models.
    
    
class Product(models.Model):
    name = models.CharField(max_length=200, help_text="Name of product")
    stock = models.IntegerField(help_text="Stock")
    price = models.IntegerField(help_text="Price", null=True)
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to="img/products")
    description = models.CharField(max_length=500, help_text="Product Description", default="Product Descr")
    

    class Meta:
        verbose_name = ("Product")

    def __str__(self):
        return f'{self.name}'


    
    
class category(models.Model):
    typeOf = models.CharField(max_length=200, help_text="Type of category")
    
    def __str__(self):
        return f'{self.typeOf}'
    
    
    
class imageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE);
    image = models.ImageField(upload_to="img/products")
    
    def __str__(self):
        return f'{Product.name}'
