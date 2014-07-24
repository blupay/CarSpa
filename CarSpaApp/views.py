from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import *
from django.template import loader, RequestContext


def index(request):
	return  render_to_response('portal/index.html',{'user':request.user})   



@csrf_exempt
def add_customer(request):
	customer_instance=None
	saved=''
	try:
		if request.method =="POST":
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
	perform_trans =None
	try:
		get_customer = Customer.objects.get(customer_ID=term)
	except Customer.DoesNotExist:
		pass
	get_services = Service_Rendered.objects.all()
	if request.method =="POST":
		save= "on"
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
				
			
		except KeyError:	
			pass
		 
		
	else:
		save = ''
	return render_to_response('portal/customer_transaction.html',	{
							'save':save,
							'get_customer':get_customer,
							'get_services':get_services,
							'perform_trans':perform_trans,
							'user':request.user})
	
			
