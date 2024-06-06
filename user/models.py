from django.db import models

class Payment(models.Model):
    txnid=models.AutoField(primary_key=True)
    uid=models.CharField(max_length=100)
    price=models.IntegerField()
    info=models.CharField(max_length=50)


class Product(models.Model):
    pid=models.AutoField(primary_key=True)
    ptitle=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    subcategory=models.CharField(max_length=50)
    baseprice=models.IntegerField()
    pdescription=models.CharField(max_length=1000)
    uid=models.CharField(max_length=100)
    info=models.CharField(max_length=50) 
    
class Bid(models.Model):
    bid=models.AutoField(primary_key=True)
    pid=models.IntegerField()
    bprice=models.CharField(max_length=50)
    cprice=models.CharField(max_length=50)
    bidprice=models.CharField(max_length=50)
    info=models.CharField(max_length=50) 
