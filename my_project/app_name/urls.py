from django.urls import include, path
from app_name import views
 
app_name = 'app_name'
 
urlpatterns = [
    path('contact_form',views.contact_form,name='contact_form'),
    path('',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('contact_form_submit',views.contact_form_submit,name='contact_form_submit')
]