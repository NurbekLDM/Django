from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
urlpatterns = [
	path('employees/', employees, name= 'employees'),
    path('company/', company, name= 'company'),
	path('contact/', contact_view, name='contact')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



