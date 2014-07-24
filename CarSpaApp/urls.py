from django.conf.urls import *
from models import *
from django.contrib.auth.views import login


urlpatterns = patterns('',
		  url(r'^$', 'CarSpaApp.views.index'),
		  #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
		  url(r'^add_customer/$', 'CarSpaApp.views.add_customer'),
		  url(r'^transactions/$', 'CarSpaApp.views.add_transaction'),
		  url(r'^search/$', 'CarSpaApp.views.search', name = 'search' ),
		  url(r'^customer/trans/(?P<term>.*?)/((?P<showDetails>.*)/)?$', 'CarSpaApp.views.customer_transaction'),
		  
		  #url(r'^accounts/login/?next=/$', 'login'),
		  		 
		  
)
  
