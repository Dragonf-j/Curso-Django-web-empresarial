from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
# Create your views here.
def contact(request):
    #print('Tipo de peticion: {}'.format(request.method))
    contactForm = ContactForm()
    if request.method == 'POST':
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name= request.POST.get('name', '')
            email= request.POST.get('email', '')
            content= request.POST.get('content', '')
            #sopones que todo fue bien y redicreccionamos
            return redirect(reverse('contacto')+"?ok") #tiene que ser el nombre que esta en urls

    return render(request,"contact/contact.html", {'form':contactForm})