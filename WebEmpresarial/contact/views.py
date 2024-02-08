from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

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
            #enviamos el correo y redirecionamos

            mail = EmailMessage(
                "la CAffetera: Nuevo mensaje de contacto", 
                "De {} <{}>\n\n{}".format(name, email, content),
                "No-contestar#inbox.mailtrap.io",
                ["jmjejuan@gmail.com"],
                reply_to=[email]
            )
            try:
                mail.send()
                return redirect(reverse('contacto')+"?Ok")
            except:
                return redirect(reverse('contacto')+"?Fail") #tiene que ser el nombre que esta en urls
                

    return render(request,"contact/contact.html", {'form':contactForm})