from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_vaild():
           form.save()
           messages.success(request,'✔Your message has been sent!')
        else:
            messages.error(request,'⚠Please fill the form correctly!')
    else:
        form  = ContactForm()
    return render(request, 'contact.html', {'form':form})