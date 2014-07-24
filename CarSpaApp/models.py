from django.db import models
from django.contrib import admin
from django.conf import settings
from datetime import date,time
import datetime
from django.utils.timezone import now
import datetime,random
from datetime import date,time



                

class Customer(models.Model):
	customer_ID = models.CharField(max_length=10,unique=True,blank=True,null=True,help_text ="Auto Generated ID")
	Full_Name = models.CharField(max_length=60, blank=False,  null =False, help_text="Enter Customer's full Name")
	email = models.EmailField(max_length=50,blank=True,null=True)
        mobile_number = models.CharField(max_length=10,blank=True,null=True, help_text='Primary')
        tel_number = models.CharField(verbose_name='Tel',max_length=10,blank=True,null=True, help_text='')
        gender = models.CharField(max_length=6, choices =(("Male","Male"),
                                                      ("Female","Female")),)
        
        date_created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
      	date_updated=models.DateTimeField(auto_now=True,blank=True,null=True)
      	
      	
      	def __unicode__(self):
              return "%s-[%s]" %(self.Full_Name.upper(),self.mobile_number)


	def to_upper(self):
      		self.Full_Name = self.Full_Name.upper()
      		return True
      		
      	def get_car_number(self):
      		get_his_car =''
      		car_numbers = []
      		try:
      			get_his_car = Car_number.objects.filter(customer__customer_ID = self.customer_ID)
      			for number in get_his_car:
      				car_numbers.append(number.car_number)
      		except Car_number.DoesNotExist:
      			pass
      		car_numbers =list(set(car_numbers))
      		return car_numbers 
      		
      	def customer_id(self):
                if self.customer_ID ==None:
			customer_id_gen = random.randint(1,1000)     
                	self.customer_ID = "%s%s" %(self.Full_Name[:2].upper(),customer_id_gen)
                else:
                	pass
                return True	
        class Meta:
		verbose_name 	    = "Customer"
		verbose_name_plural = "Customers"
		#ordering = ('date_created',)

      	def save(self,*args,**kwargs):
                self.to_upper()
                self.customer_id()
		super(Customer,self).save(*args, **kwargs)
                return True
                
class Car_number(models.Model):
	car_number = models.CharField(max_length=40, unique=True, blank = False, null =False)
	customer = models.ForeignKey(Customer,related_name='customer')
	date_created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
      	date_updated=models.DateTimeField(auto_now=True,blank=True,null=True)

	def __unicode__(self):
              return "%s" %(self.car_number)


	def to_upper(self):
      		self.car_number = self.car_number.upper()
      		return True
      		
        class Meta:
		verbose_name 	    = "Car Number"
		verbose_name_plural = "Car Numbers"

      	def save(self,*args,**kwargs):
                self.to_upper()
                
		super(Car_number,self).save(*args, **kwargs)
                return True
                
                
                
                
class Worker(models.Model):
      work_ID 		=  models.CharField(max_length=10,blank=True,null=True,help_text ="Generated ID")
      Full_Name 	= models.CharField(max_length=60, blank=False, default="Yaw", null =False, help_text="Enter Worker's full Name")
      work_detail 	= models.TextField('Work Details')
      email 		= models.EmailField(max_length=50,unique=True,blank=True,null=True)
      mobile_number 	= models.CharField(max_length=10,blank=True,null=True)
      residentialAddress = models.TextField(verbose_name ='Residential Address',blank=True,null=True)
      gender 		= models.CharField(max_length=6, choices =(("Male","Male"),
                                                      ("Female","Female")),)
      date_Of_birth  	=  models.DateField(blank = True, null = True,help_text = "")
      age            	=  models.PositiveIntegerField(blank = True, null = True,help_text ="Generated from date of birth")
      place_Of_birth 	=  models.CharField("Place Of Birth", max_length = 30, blank = True, null = True, help_text="City/Town")
     # Nationality    =  models.ForeignKey(Country, default = "GH", related_name = "count")
      religion       	=  models.CharField('Religion', 
                                            choices =(("Christianity","Christianity"),
                                                      ("Islam","Islam"),
                                                      ("Buddhism","Buddhism"),
						      ("Hinduism","Hinduism"),
						      ("Judaism","Judaism"),
						      ("Rastafari_Movement","Rastafari Movement"),
						      ("Jainism","Jainism"),
						      ("Shinto","Shinto"),
						      ("Other","Other")),
					     max_length = 20)
      blood_group   	= models.CharField('Blood Group', 
                                          choices =(("O+","O+"),
                                                    ("A+","A+"),
                                                    ("B+","B+"),
						    ("AB+","AB+"),
						    ("O-","O-"),
                                                    ("A-","A-"),
                                                    ("B-","B-"),
						    ("AB-","AB-")),
					     max_length = 3)
      nextOfKin 	= models.TextField(verbose_name='Next of Kin',blank=True,null=True)
      employment_date 	= models.DateField(blank = True, null = True,help_text = "") 
      date_created	= models.DateTimeField(auto_now_add=True,blank=True,null=True)
      date_updated	= models.DateTimeField(auto_now=True,blank=True,null=True)
      
      

      def to_upper(self):
      		self.Full_Name = self.Full_Name.upper()
      		return True
      		
      		
      def worker_ID(self):
                if self.work_ID ==None:
			work_id_gen = random.randint(1,1000)     
                	self.work_ID = "%s%s" %(self.Full_Name[:2].upper(),work_id_gen)
                else:
                	pass
                return True

      def __unicode__(self):
              return "%s-%s" %(self.work_ID,self.Full_Name.upper())


	
      class Meta:
		verbose_name 	    = "Car Spa WORKER"
		verbose_name_plural = "Car Spa Workers"


      def Age(self):
		if self.date_Of_birth:
	                 min_allowed_dob = datetime.datetime(1900,01,01)
	         	 max_allowed_dob = datetime.datetime.now()
			 if int(self.date_Of_birth.strftime("%G")) >= int( min_allowed_dob.strftime("%G") ) and int(self.date_Of_birth.strftime("%G")) <= int(max_allowed_dob.strftime("%G")):
               			 self.age  = "%s" %(int(max_allowed_dob.strftime("%G"))-  int(self.date_Of_birth.strftime("%G")))
               			 return "%s" %(self.age)
                             
			 else:
			 	return "Invalid Date"
		elif self.age and int(self.age[0:3])<=120: #no need cos age field was not added for the doctor. would be added later
	        	self.date_Of_birth = None
		        return True

      def save(self,*args,**kwargs):
                self.to_upper()
                self.worker_ID()
		self.Age()
		super(Worker,self).save(*args, **kwargs)
                return True
                

class Service_Category(models.Model):
	category_name 	= models.CharField(max_length=20,blank=True,null=True,help_text ="")
        date_created 	= models.DateTimeField(auto_now_add=True,blank=True,null=True)
        date_updated 	= models.DateTimeField(auto_now=True,blank=True,null=True)

	def __unicode__(self):
              return "%s" %(self.category_name)

	def to_upper(self):
      		self.category_name = self.category_name.upper()
      		return True
      		
	class Meta:
		verbose_name 	    = "Service Category"
		verbose_name_plural = "Service Categories"
		
	def save(self,*args,**kwargs):
                self.to_upper()
                
		super(Service_Category,self).save(*args, **kwargs)
                return True
                
		
class Wash_Type(models.Model):
        name 		= models.CharField(unique=True,max_length=20,blank=True,null=True,help_text ="")
        date_created 	= models.DateTimeField(auto_now_add=True,blank=True,null=True)
        date_updated 	= models.DateTimeField(auto_now=True,blank=True,null=True)

	def __unicode__(self):
              return "%s" %(self.name)
              
        class Meta:
		verbose_name 	    = "Wash Type"
		verbose_name_plural = "Wash Types"
	
	
	def to_upper(self):
      		self.name = self.name.upper()
      		return True
      		
      			
	def save(self,*args,**kwargs):
                self.to_upper()
                
		super(Wash_Type,self).save(*args, **kwargs)
                return True
        
class Car_Type(models.Model):
        name 		= models.CharField(max_length=20,blank=True,null=True,help_text ="")
        date_created 	= models.DateTimeField(auto_now_add=True,blank=True,null=True)
        date_updated 	= models.DateTimeField(auto_now=True,blank=True,null=True)

	def __unicode__(self):
              return "%s" %(self.name)
        
        class Meta:
		verbose_name 	    = "Car Type"
		verbose_name_plural = "Car Types"
	
	def to_upper(self):
      		self.name = self.name.upper()
      		return True
      		
      			
	def save(self,*args,**kwargs):
                self.to_upper()
                
		super(Car_Type,self).save(*args, **kwargs)
                return True


class Service_Rendered(models.Model):
	serviceID  	= models.CharField(max_length=10,blank=True,null=True,help_text ="Generated ID")
	
	service_Name 	= models.ForeignKey(Wash_Type,verbose_name="Wash Type",max_length=30,blank=True,null=True)
	car_type 	= models.ForeignKey(Car_Type)
	description 	= models.TextField(blank=True,null=True)
	category 	= models.ForeignKey(Service_Category)
	
	
	price =  models.FloatField(blank = True, null = True,help_text ="Service Price")
	date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
        date_updated = models.DateTimeField(auto_now=True,blank=True,null=True)


	class Meta:
		verbose_name 	    = "CAR SPA SERVICE"
		verbose_name_plural = "CAR SPA Services"
		unique_together     =('service_Name','car_type')
		ordering            = ('-category','-date_created',)

        
      		
	def service_ID(self):
	        if self.serviceID == None:
			servc_id_gen = random.randint(1,100)     
                	self.serviceID = "%s%s" %(self.service_Name.name[:2].upper(),servc_id_gen)
                else:
                	pass
                return True

	def __unicode__(self):
              return "[%s]-%s-[GHS %s]" %(self.car_type.name,self.service_Name,self.price)

	def save(self,*args,**kwargs):
                self.service_ID()
                
		super(Service_Rendered,self).save(*args, **kwargs)
                return True



class Transaction(models.Model):
	TransID 	= models.CharField(max_length=20,blank=True,null=True,help_text ="Generated ID")
        amount 		= models.FloatField(default=0.0,blank = True, null = True,help_text ="Amount GHC")
        customer 	= models.ForeignKey(Customer)
	attendance 	= models.CharField(max_length=20,blank=True,null=True)
	date_created 	= models.DateTimeField(verbose_name='Date & Time',auto_now_add=True,blank=True,null=True)
        date_updated 	= models.DateTimeField(auto_now=True,blank=True,null=True)
	
        class Meta:
		verbose_name 	    = "CAR SPA TRANSACTION"
		verbose_name_plural = "Car Spa Transactions"


	def Trans_ID(self):
		Trans_id_gen = random.randint(1,10000000)     
                self.TransID = "SPA%sTX" %(Trans_id_gen)
                return True

	def totalService(self):
            totalService = 0
            for tot in self.transaction.all():
                totalService += tot.totalService()
            return totalService
                     

        def totalAmount(self):
            totalAmount=0
            totalAmount = self.totalService()
            self.amount = self.totalService()
            return totalAmount
  
	def __unicode__(self):
              return self.TransID
              
        


	def save(self,*args,**kwargs):
                self.Trans_ID()
                self.totalService()
                self.totalAmount()
		super(Transaction,self).save(*args, **kwargs)
                return True


class Reset_Star_Point(models.Model):
	value = models.IntegerField(verbose_name='Max Point',help_text="Change with caution")
	saloon_value =models.IntegerField(verbose_name='Saloon Per Wash Point(s)',help_text="Point(s) for saloon cars per wash")
	suv_value =models.IntegerField(verbose_name='SUV Per Wash Point(s)',help_text="Point(s) for suv  per wash")
	date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
        date_updated = models.DateTimeField(auto_now=True,blank=True,null=True)
        
	def __unicode__(self):
              return str(self.date_created)
	
	class Meta:
		verbose_name 	    = "Reset Star Point"
		verbose_name_plural = "Reset Star Points"


class Star_Point(models.Model):
	customer = models.ForeignKey(Customer)
	point    = models.IntegerField()
	status   = models.CharField(choices =(("Star","Star"),("StarV","StarV"),("StarP","StarP"),),max_length=10)
	count    = models.IntegerField(default=0)
	date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
        date_updated = models.DateTimeField(auto_now=True,blank=True,null=True)
        
	def __unicode__(self):
              return self.customer.Full_Name
              
        class Meta:
		verbose_name 	    = "Star Point"
		verbose_name_plural = "Star Points"
		
		
class ServiceTransaction(models.Model):
	servcTransID 	= models.CharField(max_length=20,blank=True,null=True,help_text ="Generated ID")
	worker 		= models.ForeignKey(Worker, blank=True, null =True,related_name="worker")
	service 	= models.ForeignKey(Service_Rendered,related_name="service" )
	#customer= models.ForeignKey()
	#star_point	= models.ForeignKey(Star_Point)
        Transxn		= models.ForeignKey(Transaction, related_name="transaction")
	date_created 	= models.DateTimeField(auto_now_add=True,blank=True,null=True)
        date_updated 	= models.DateTimeField(auto_now=True,blank=True,null=True)
	
        class Meta:
		verbose_name 	    = "CAR SPA SERV-TRANS"
		verbose_name_plural = "Car Spa Serv-Trans"

	def accummulate_point(self):
	        
	        try:
	        	check_this_customer = Star_Point.objects.get(customer=self.Transxn.customer)
	        	
	        	GET_value =Reset_Star_Point.objects.get(pk=1)
	    
	        	get_existing_point = check_this_customer.point
	        	get_new_value = get_existing_point + GET_value.value
	        	print get_new_value
	        	if get_existing_point < GET_value.value:
	        	        if self.service.car_type.name == "SALOON":
					check_this_customer.point = GET_value.saloon_value + get_existing_point
					check_this_customer.status = "Star"
					check_this_customer.save()
				elif self.service.car_type.name == "SUV":
					check_this_customer.point = GET_value.suv_value + get_existing_point
					check_this_customer.status = "Star"
					check_this_customer.save()
			elif get_new_value == GET_value.value:
				check_this_customer.point = 0.0
				check_this_customer.status = "StarP"
				check_this_customer.count  += check_this_customer.count
				check_this_customer.save()
			
			elif get_new_value > GET_value.value:
				diff = get_existing_point-GET_value.value
				check_this_customer.point = diff
				check_this_customer.count  = check_this_customer.count+1
				check_this_customer.status="Star"
				check_this_customer.save()
	        except Star_Point.DoesNotExist:
	        	GET_value =Reset_Star_Point.objects.get(pk=1)
	        	get_star = Star_Point()
			get_star.customer  = self.Transxn.customer
			if self.service.car_type.name == "SALOON":
				get_star.point     = GET_value.saloon_value
				get_star.status    = "Star"
				get_star.save()
			elif self.service.car_type.name == "SUV":
				get_star.point     = GET_value.suv_value
				get_star.status    = "Star"
				get_star.save()
			
		return True 
			
	def servcTrans_ID(self):
	        if self.servcTransID ==None:
			servcTrans_id_gen = random.randint(1,100000000)     
                	self.servcTransID = "TRANS%s" %(servcTrans_id_gen)
                else:
                	pass
                return True
        
        
        
        def totalService(self):
            return self.service.price

	def __unicode__(self):
              return self.servcTransID


	def save(self,*args,**kwargs):
                self.servcTrans_ID()
                self.accummulate_point()
                            
		super(ServiceTransaction,self).save(*args, **kwargs)
               # self.Transxn.amount = self.Transxn.totalService()
                #self.Transxn.service_rendered.save()
                self.Transxn.save()
                
                return True


        



