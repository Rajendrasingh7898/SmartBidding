from django.db import models

class Category(models.Model):
    categoryid=models.AutoField(primary_key=True)
    categoryname=models.CharField(max_length=50,unique=True)
    categoryicon=models.CharField(max_length=100)

class subCategory(models.Model):
    subcategoryid=models.AutoField(primary_key=True)
    subcategoryname=models.CharField(max_length=50,unique=True)
    categoryname=models.CharField(max_length=50  )
    subcategoryicon=models.CharField(max_length=100)

class Addproduct(models.Model):
    pid=models.AutoField(primary_key=True)
    atitle=models.CharField(max_length=50)
    acategory=models.CharField(max_length=50)
    adescription=models.CharField(max_length=100)
    baseprice=models.CharField(max_length=50)
    info=models.CharField(max_length=50)