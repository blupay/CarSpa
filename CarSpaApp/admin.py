from django.contrib import admin
from CarSpaApp.models import *
from django.forms import ModelForm,TextInput 
from suit.widgets import SuitDateWidget,LinkedSelect, SuitTimeWidget, SuitSplitDateTimeWidget,HTML5Input,AutosizedTextarea,EnclosedInput
from suit.admin import SortableTabularInline
# Register your models here.

class ChangeWorkerForm(ModelForm):
    class Meta:
       
        widgets = {
            'employment_date': HTML5Input(input_type='date'),
            'residentialAddress': AutosizedTextarea,
            'nextOfKin':AutosizedTextarea,
            'work_detail':AutosizedTextarea,
            'date_Of_birth':HTML5Input(input_type='date'),
            'email': EnclosedInput(append='icon-envelope'),
            
        }
        
class Worker_Admin(admin.ModelAdmin):
      form = ChangeWorkerForm
      list_display = ('work_ID','Full_Name','mobile_number','gender','date_Of_birth','Age','employment_date','date_created')
      list_filter = ('gender','date_created',)
      ordering = ['-date_created']
      date_hierarchy    = 'date_created'
      search_fields = ['Full_Name','email','mobile_number',]
      #fieldsets         = ( ("Worker Personal Details", {'fields':('username','firstname','lastname', 'email', 'mobile_number','department',)}),)
      readonly_fields       = ('age','work_ID')
      
      

class Service_Rendered_Admin(admin.ModelAdmin):
      list_display = ('serviceID','service_Name','car_type','price','date_created','date_updated')
      list_filter = ('service_Name','date_created',)
      ordering = ['-date_created']
      date_hierarchy    = 'date_created'
      search_fields = ['service_Name','serviceID','description',]
      #fieldsets         = ( ("User Details", {'fields':('username','firstname','lastname', 'email', 'mobile_number','department',)}),)
      readonly_fields       = ('serviceID',)  
      
      
class ServcTransInline(admin.TabularInline):
      model = ServiceTransaction
      fields = [('worker', 'service','servcTransID',),]
      readonly_fields = ('Transxn','servcTransID',)
      #raw_id_fields = ('service',)
      extra= 1
      
class CarNumberInline(admin.TabularInline):
      model = Car_number
      extra= 1

class Customer_Admin(admin.ModelAdmin):
      list_display = ('customer_ID','Full_Name','mobile_number','gender','date_created','date_updated')
      list_filter = ('date_created',)
      ordering = ['-date_created',]
      date_hierarchy    = 'date_created'
      search_fields = ['Full_Name','mobile_number',]
      readonly_fields       = ('customer_ID',)
      inlines           = [CarNumberInline,]


class ServiceTransaction_Admin(admin.ModelAdmin):
      list_display = ('servcTransID','worker','service','date_created','date_updated')
      list_filter = ('date_created',)
      ordering = ['-date_created']
      date_hierarchy    = 'date_created'
      search_fields = ['servcTransID','worker','^service__service_Name',]
      #fieldsets         = ( ("User Details", {'fields':('username','firstname','lastname', 'email', 'mobile_number','department',)}),)
      readonly_fields       = ('servcTransID',)
      #raw_id_fields = ('service',)     
      
      

class Transaction_Admin(admin.ModelAdmin):
      obj = Transaction()
      def save_model(self,request,obj,form,change):
                obj.attendance = request.user.username
                obj.save()

      fields = [('TransID', 'amount','attendance','customer',),]
      list_display = ('TransID','customer','amount','attendance','date_created',)
      list_filter = ('date_created',)
      ordering = ['-date_created']
      date_hierarchy    = 'date_created'
      search_fields = ['TransID','amount','attendance',]
      #fieldsets         = ( ("User Details", {'fields':('username','firstname','lastname', 'email', 'mobile_number','department',)}),)
      inlines           = [ServcTransInline,]
      readonly_fields       = ('TransID','attendance','amount',)      
      
      
class Reset_Star_Point_Admin(admin.ModelAdmin):
	list_display=('value','saloon_value','suv_value',)
	fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['value',]}),
        (None, {
            'classes': ('suit-tab suit-tab-Saloon',),
            'fields': ['saloon_value',]}),
        (None, {
            'classes': ('suit-tab suit-tab-suv',),
            'fields': ['suv_value',]}),
         
         
    ]
	suit_form_tabs = (('general','General Settings'),('Saloon', 'SALOON'), ('suv', 'SUV'))     
      
      
class Star_Point_Admin(admin.ModelAdmin):
	list_display = ('customer','point','status','count','date_created',)
      	list_filter = ('date_created','point',)
      	ordering = ['-date_created']
      	date_hierarchy    = 'date_created'
      	search_fields = ['^customer__Full_Name',]
      
      
         
admin.site.register(Customer,Customer_Admin)
admin.site.register(Star_Point, Star_Point_Admin)
admin.site.register(Reset_Star_Point, Reset_Star_Point_Admin)

admin.site.register(Service_Category)
admin.site.register(Wash_Type)
admin.site.register(Car_Type)
admin.site.register(Service_Rendered,Service_Rendered_Admin)
admin.site.register(Worker,Worker_Admin)

admin.site.register(ServiceTransaction,ServiceTransaction_Admin)
admin.site.register(Transaction,Transaction_Admin)
