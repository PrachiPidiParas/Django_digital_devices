from django.db import models
class Customer(models.Model):
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
    @staticmethod
    def get_customer_byEmail(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False