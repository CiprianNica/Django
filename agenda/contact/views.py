from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def index(request):
    #contacts = Contact.objects.all()
    contacts = Contact.objects.filter(name__contains=request.GET.get('search',''))
    context = {'contacts':contacts}
    return render(request, 'contact/index.html', context)

def view(request, id):
    contact = Contact.objects.get(id=id)
    context = {'contact':contact}
    return render(request, 'contact/detail.html', context)

def delete(request, id):
    contact = Contact.objects.get(id=id)
    
    if request.method == 'GET':
        form = ContactForm(instance=contact)
        context = {
            'form':form,
            'id':id
            }
        messages.warning(request, 'Seguro quieres borrar ?.')
        return render(request, 'contact/delete.html', context)
    
    contact.delete()
    
    if request.method == 'POST':
        contact = Contact.objects.all()
        #context = {'contact':contact}
        messages.success(request, 'Contacto borrado con exito.')
        return redirect('contact')
        
def edit(request, id):
    contact = Contact.objects.get(id=id)
    
    if request.method == 'GET':
        form = ContactForm(instance=contact)
        context = {
            'form': form,
            'id': id
            }
        return render(request, 'contact/edit.html', context)
    
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        form.save()
        context = {
            'form':form,
            'id':id
            }  
        
        messages.success(request, 'Contacto actualizado.')
        return render(request, 'contact/edit.html', context)
    
def create(request):
    if request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact/create.html', context)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
        context = {
            'form':form,
            }
    messages.success(request, 'Contacto creado con exito.')
    #return render(request, 'contact/create.html', context)
    return redirect('contact')