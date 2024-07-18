from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=20)

    @staticmethod
    def get_customer_by_email(email):
        try:
           return Customer.objects.get(email=email)
        except:
         return False
        

    def  isExist(self):
       if Customer.objects.filter(email=self.email):
          return True
       else:
          return False
       
       
           


    
