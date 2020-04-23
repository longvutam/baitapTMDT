from django.db import models


# Create your models here.



# class product(models.Model):
#     id_pro = models.IntegerField("id")
#     name_pro = models.CharField("Product Name", max_length=500)
#     price_pro = models.IntegerField("Price", default=0)
#     quantity = models.IntegerField("Quantity", default=0)
#     description = models.TextField("Description")
#     img_pro = models.ImageField("image",max_length = 255)
#     id_cart = models.ForeignKey(cart, on_delete = models.CASCADE)
    
#     def __str__(self):
#         return self.name

# # class cart(models.Model):
# #     id_cart = models.IntegerField("id")
    

# # class offer(models.Model):
# #     id_offer = models.IntegerField("id")
# #     firstname_user = models.CharField("Product Name", max_length=20)
# #     lastname_user = models.CharField("Product Name", max_length=20)
# #     address_user = 
    