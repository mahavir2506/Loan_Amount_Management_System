from django.shortcuts import render
from django.http import HttpResponse
import datetime
from datetime import date,timedelta
from account.models import account
def numberOfDays(y, m):
      leap = 0
      if y% 400 == 0:
         leap = 1
      elif y % 100 == 0:
         leap = 0
      elif y% 4 == 0:
         leap = 1
      if m==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30
def finalammount(idate,ammount,iammount):
	start_date = idate
	last_date=date.today()
	ammount=ammount
	interest_ammount=iammount
	diff=last_date.month-start_date.month
	if(diff<=0 or start_date.year!=last_date.year):
		diff=diff+(last_date.year-start_date.year)*12
	for i in range(0,diff):
		days=numberOfDays(start_date.year,start_date.month)
		if( start_date+timedelta(days=days)<=last_date):
			start_date=start_date+timedelta(days=days)
			ammount=ammount+iammount
	return start_date,ammount         

def index(request):
	if(request.method=="POST"):
		try:
			a=account()
			a.name=request.POST["name"]
			a.mother_name=request.POST["mother name"]
			a.father_name=request.POST["father name"]
			a.spouse_name=request.POST["spouse name"]
			a.nominee_name=request.POST["nominee name"]
			a.mobile_no=request.POST["mobile"]
			a.aadharcard=request.POST["aadharcard"]
			a.pancard=request.POST["pan card"]
			a.gender=request.POST["gender"]
			if(request.POST["checkbook"]=="yes"):
				a.checkbook=True
			else:
				a.checkbook=False
			a.address=request.POST["address"]
			a.spouse_bod=request.POST["spouse birth date"]
			if(request.POST["married"]=="married"):
				a.married_status=True
			else:
				a.married_status=False
			a.education=request.POST["education"]
			a.caste=request.POST["caste"]
			a.annual_income=request.POST["income"]
			a.ammount=request.POST["ammount"]
			a.interest_ammount=float((float(request.POST["interest"])/100)*float(request.POST["ammount"]))
			a.occupation=request.POST["occupation"]
			a.place_of_birth=request.POST["place of birth"]
			a.income_category=request.POST["income category"]
			a.nature_of_barring=request.POST["nature"]
			a.loan_date=datetime.date.today()
			a.interest_date=datetime.date.today()
			a.profile=request.FILES["profile"]
			a.distric=request.POST["distric"]
			a.save()
			b=account.objects.get(name=request.POST["name"],aadharcard=request.POST["aadharcard"])
			return render(request,"index.html",{"cid":b.cid})
		except:
			return render(request,"index.html",{"cid":"Something Wrong"})
	else:
		z=account.objects.all()
		for i in z:
			c=account.objects.get(cid=i.cid)
			c.interest_date,c.ammount=finalammount(c.interest_date,c.ammount,c.interest_ammount)
			c.save()
		return render(request,"index.html")
def search(request):
	if request.method=="POST":
		try:
			c=account.objects.get(cid=request.POST["cid"])
			list1=[]
			d={}
			d["name"]=c.name
			d["ammount"]=c.ammount
			d["aadharcard"]=c.aadharcard
			d["interest_ammount"]=c.interest_ammount
			d["interest_date"]=c.interest_date
			list1.append(d)
			return render(request,"search.html",{"list":list1})
		except:
			return render(request,"search.html",{"error":"Data Not Found"}) 
	else:
		z=account.objects.all()
		for i in z:
			c=account.objects.get(cid=i.cid)
			c.interest_date,c.ammount=finalammount(c.interest_date,c.ammount,c.interest_ammount)
			c.save()
		return render(request,"search.html")
def deposite(request):
	if request.method=="POST":
		try:
			c=account.objects.get(cid=request.POST["cid"])
			if(c.ammount<int(request.POST["ammount"]) or int(request.POST["ammount"])<=0):
				return render(request,"deposite.html",{"error":"Not Sufficient Ammount"})
			else:
				c.ammount=c.ammount-int(request.POST["ammount"])
				c.save()
				return render(request,"deposite.html",{"error":"Succesfull....."})
		except:
			return render(request,"deposite.html",{"error":"Data is not found"})
	else:
		z=account.objects.all()
		for i in z:
			c=account.objects.get(cid=i.cid)
			c.interest_date,c.ammount=finalammount(c.interest_date,c.ammount,c.interest_ammount)
			c.save()
		return render(request,"deposite.html")
def list(request):
	z=account.objects.all()
	for i in z:
		c=account.objects.get(cid=i.cid)
		c.interest_date,c.ammount=finalammount(c.interest_date,c.ammount,c.interest_ammount)
		c.save()
	d=account.objects.all()
	return render(request,"list.html",{"d":d})