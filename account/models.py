from django.db import models

class account(models.Model):
	cid=models.AutoField(primary_key=True)
	name=models.CharField(max_length=100)
	mother_name=models.CharField(max_length=100,default="None")
	father_name=models.CharField(max_length=100)
	spouse_name=models.CharField(max_length=100,default="None")
	nominee_name=models.CharField(max_length=100)
	mobile_no=models.IntegerField()
	aadharcard=models.IntegerField()
	pancard=models.CharField(max_length=30,blank=True,default="None")
	gender=models.CharField(max_length=10)
	checkbook=models.BooleanField(default=False)
	address=models.CharField(max_length=200)
	spouse_bod=models.DateField(default="01/01/1970")
	married_status=models.BooleanField(default=True)
	education=models.CharField(default="None",max_length=50)
	caste=models.CharField(max_length=10)
	annual_income=models.IntegerField()
	ammount=models.FloatField()
	interest_ammount=models.FloatField()
	occupation=models.CharField(max_length=20)
	place_of_birth=models.CharField(max_length=20)
	income_category=models.CharField(max_length=100)
	nature_of_barring=models.CharField(max_length=100)
	loan_date=models.DateField()
	interest_date=models.DateField()
	profile=models.ImageField(upload_to="imgs/",blank=True)
	distric=models.CharField(max_length=10,default="None")



	"""docstring for """

