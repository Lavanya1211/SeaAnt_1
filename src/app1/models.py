from django.db import models
from django.contrib.auth.models import User

class Contact_Us(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    class Meta:
        db_table = "query"



class PhoneBook(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.BigIntegerField()
    address = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    datamode = models.CharField(max_length=1, default='A', choices=(('A','Active'),('I','Inactive'),('D','Deleted')))
    class Meta:
        db_table = "phone_book"