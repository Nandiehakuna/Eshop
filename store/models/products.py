from django.db import models
from .category import Category

class Product(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=30, default='', blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE )
    image=models.ImageField(upload_to='uploads/products')
    price=models.IntegerField()

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.object.all()
    
    @staticmethod
    def get_products_by_category(category_id):
        if category_id:
         return Product.objects.filter(category=category_id)
        
        else:
           return Product.get_all_products
        
        
        

    


    



