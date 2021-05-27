from django.shortcuts import render, redirect
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib import messages

def ContactCreateView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your message has been sent!')
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
        return render(request, "contact/contact.html", {'form': form})