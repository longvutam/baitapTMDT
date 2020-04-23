from django.db import models

class Product(models.Model):
    name_pro = models.CharField(max_length=500)
    price_pro = models.IntegerField(default=0)
    description = models.TextField()
    img_pro = models.ImageField(upload_to='imgProduct')
    def __str__(self):
        return self.name_pro
    

class Transaction(models.Model):
    firstname_user = models.CharField("first name", max_length=20)
    lastname_user = models.CharField("last name", max_length=20)
    address_user = models.TextField("Address", max_length=300)
    phone_user = models.CharField("Phone Number", max_length=10)
    amount = models.IntegerField("amout", default=0)
    message = models.TextField("Message", max_length=300)
    Order = models.ManyToManyField(Product, through='Order')
    def __str__(self):
        return self.lastname_user
   

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete = models.CASCADE)
    amount = models.IntegerField("amout", default=0)
    priceOrder = models.IntegerField()
    def __str__(self):
        return self.priceOrder
   
