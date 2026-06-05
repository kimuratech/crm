from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.shortcuts import redirect


def contact_list(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact-list')
    else:
        form = ContactForm()
    contacts = Contact.objects.all()
    return render(request, 'contacts/list.html', {'contacts': contacts, 'form': form})
