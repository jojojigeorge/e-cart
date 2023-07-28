from django.db import models
import os
import datetime
# Create your models here.

class Tables(models.Model):
    table_name=models.CharField(max_length=100)
    status=models.BooleanField(default=False,help_text="0-free table, 1-occupied")
    all_item_delivered=models.BooleanField(default=False,help_text=" 1-complete")
    paid=models.BooleanField(default=False,help_text="0-not paid, 1-paid")

    def __str__(self):
        return str(self.table_name)
    
def get_file_path(request,filename):
    original_filename=filename
    nowTime=datetime.datetime.now().strftime(' %Y%m%d%H:%M:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/',filename)  


class Categories(models.Model):
    category_name = models.CharField(max_length=150,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-active category, 1-non active")

    def __str__(self):
        return str(self.category_name)
    

class Items(models.Model):
    
    item_name=models.CharField(max_length=150)
    category=models.ManyToManyField(Categories)
    initial_stock=models.IntegerField()
    item_remain=models.IntegerField()
    item_price=models.FloatField()
    item_description = models.CharField(max_length=250,null=True)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0-in stock, 1-out of stock")
    ordered=models.BooleanField(default=False,help_text="0-not selected, 1-selected")
    selected_itm=models.IntegerField(default=0)

    # joji=models.CharField(max_length=150,default=4)

    def __str__(self):
        return str(self.item_name)



    

class Orders(models.Model):
    customer_name = models.CharField(max_length=150,null=True,blank=True)
    table = models.ForeignKey(Tables,on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    delivered=models.BooleanField(default=False,help_text="0-Processing, 1-Delivered")
    order_note = models.CharField(max_length=250,null=True,blank=True)
    ordered=models.BooleanField(default=False,help_text="0-Default, 1-order placed")


    def __str__(self):
        return '{}-{}-{}-{}' .format (self.table.table_name,self.item.item_name,self.quantity,self.delivered)




class Delivered(models.Model):
    customer_name = models.CharField(max_length=150,null=True,blank=True)
    table = models.ForeignKey(Tables,on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    order_note = models.CharField(max_length=250,null=True,blank=True)
    paid=models.BooleanField(default=False,help_text="0-Default, 1-paid")


    def __str__(self):
        return '{}-{}-{}-{}' .format (self.table.table_name,self.item.item_name,self.quantity,self.paid)




 

    
