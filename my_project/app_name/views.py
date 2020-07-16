from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from app_name.models import ContactForm 

def contact_form(request):
    return render(request,'app_name/contact_form.html')

def about(request):
    return render(request, 'app_name/about.html')

def contact(request):
    return render(request,'app_name/contact.html')

def portfolio(request):
    return render(request,'app_name/portfolio.html')

def contact_form_submit(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email_id = request.POST['email_id']
        contact_number = request.POST['contact_number']
        message = request.POST['message']
        ContactForm.objects.create(full_name=full_name,
                                   email_id=email_id,
                                   contact_number=contact_number,
                                   message=message
                                   )
    return HttpResponseRedirect(reverse('app_name:contact'))