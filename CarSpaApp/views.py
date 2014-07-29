from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.template import loader, RequestContext
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect

def index(request):
	return  render_to_response('portal/index.html',{'user':request.user})   



@csrf_exempt
def add_customer(request):
	customer_instance=None
	saved=''
	this_car =None
	check_car_number=''
	car_exist=''
	try:
		if request.session['car_exist']=='on':
			car_exist ='on'
			check_car_number =request.session['check_car_number']
			print check_car_number
			
	except KeyError:
		request.session['car_exist'] =''
		car_exist =''
	try:
		if request.method =="POST":
		        try:
		                
		        	request.session['check_car_number']= request.POST['number']
		        	try:
		        		this_car = Car_number.objects.get(car_number=request.session['check_car_number'].upper())
		        		request.session['car_exist'] ='on'
		        		
		        		return HttpResponseRedirect('/add_customer/')
		        	except Car_number.DoesNotExist:
		        		pass
		        except KeyError:
		        	pass
		        	 
			saved= "on"
			customer_instance = Customer()
			try:
				get_full_name = request.POST['name']
				customer_instance.Full_Name = get_full_name
				
					
				get_email     = request.POST['email']
				customer_instance.email = get_email 
				
				get_number    = request.POST['mobile']
				customer_instance.mobile_number = get_number
				
				get_gender    = request.POST['gender']
				customer_instance.gender =get_gender
				customer_instance.save()
				car_instance = Car_number()
				get_car_number = request.POST['number']
				car_instance.car_number = get_car_number
				car_instance.customer = customer_instance
				car_instance.save()
				
			except KeyError:
				pass
	except KeyError:
		pass
	
	return  render_to_response('portal/add_customer.html',	{
								'customer_instance':customer_instance,
								'saved':saved,
								'check_car_number':check_car_number,
								'car_exist':car_exist,
								'this_car':this_car,
								'user':request.user}) 



@csrf_exempt
def add_transaction(request):
	try:
		get_reg_customers = Customer.objects.all()
	except Customer.DoesNotExist:
		pass
	return  render_to_response('portal/transactions.html',{
									'get_reg_customers':get_reg_customers,
									'user':request.user})

from django.db.models import Q
def search(request):
	q  = request.GET.get('q')
	if q is not None:
		results = Customer.objects.filter(
			Q(Full_Name__icontains =q)|
			Q(mobile_number__icontains =q)|
			Q(customer__car_number__icontains =q))
			
		return render_to_response('portal/results.html', {'results': results},context_instance = RequestContext(request))



@csrf_exempt		
def customer_transaction(request, term, showDetails=False):
	save =''
	redirect=''
	perform_trans =None
	#get_customer =None
	get_term =''
	try:
		
		get_customer = Customer.objects.get(customer_ID=term)
		request.session['term'] =term
		
	except Customer.DoesNotExist:
		pass
	'''
		try:
			if request.session['term']!='':
				get_customer = Customer.objects.get(customer_ID=request.session['term'])
				redirect = 'on'
		except KeyError:
			request.session['term'] =''
	'''	
	get_services = Service_Rendered.objects.all()
	
	if request.method =="POST":
		#Save this transaction instance
		perform_trans = Transaction()
		perform_trans.customer = get_customer
		perform_trans.attendance=request.user.username
		perform_trans.save()
		try:
			for key in request.POST:
				get_selected_service=Service_Rendered.objects.get(pk=key)
				serv_trans = ServiceTransaction()
				#system work if worker with pk=1 is not added
				serv_trans.worker=None
				serv_trans.service=get_selected_service
				serv_trans.Transxn=perform_trans
				serv_trans.save()
				save= "on"			
				request.session['term'] =''
			request.session['save_trans_pk']=perform_trans.pk
			return HttpResponseRedirect('/customer/print/transaction/'+str(get_customer.customer_ID)+'/True')
				
			
		except KeyError:	
			pass
		return HttpResponseRedirect('/customer/trans/'+str(get_customer.customer_ID)+'/True')
		 
		
	else:
		save = ''
	return render_to_response('portal/customer_transaction.html',{
							'save':save,
							'redirect':redirect,
							'get_customer':get_customer,
							'get_services':get_services,
							'perform_trans':perform_trans,
							'user':request.user})
	
def print_transaction(request, term, showDetails=False):
	get_this_trans  =None
	get_customer=None
	get_services=None
	try:
		get_customer = Customer.objects.get(customer_ID=term)
	
	except Customer.DoesNotExist:
		pass
	try:
		if request.session['save_trans_pk']!='':
			try:
				get_this_trans = Transaction.objects.get(pk=request.session['save_trans_pk'])
				try:
					get_services=ServiceTransaction.objects.filter(Transxn__pk=get_this_trans.pk)
				except ServiceTransaction.DoesNotExist:
					pass
			except Transaction.DoesNotExist:
				pass
	except KeyError:
		request.session['save_trans_pk']=''
	return render_to_response('portal/print_transaction.html',{
								'get_customer':get_customer,
								'get_services':get_services,
								'get_this_trans':get_this_trans,
								'user':request.user})		
