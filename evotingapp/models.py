from django.db import models

# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.CharField(primary_key=True,max_length=50)
    message=models.TextField(default='')
    class Meta:
       db_table="contact" 
class Users(models.Model):
    voterid=models.CharField(max_length=5)
    dob=models.CharField(max_length=10)
    class Meta:
       db_table="users"

class Regdetails(models.Model):
    voterid=models.CharField(max_length=5)
    issuedate=models.CharField(max_length=10)
    vname=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    dob=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    category=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    vidname=models.CharField(max_length=50)
    class Meta:
        db_table= "regdetails"
class VoterIds(models.Model):
    voterid=models.CharField(max_length=5)
    issuedate=models.CharField(max_length=10)
    dob=models.CharField(max_length=10)
    class Meta:
        db_table= "voterids"

class Verification(models.Model):
    mobilenumber=models.CharField(max_length=13)
    aadharnumber=models.CharField(max_length=12)
    class Meta:
        db_table = "verification"
