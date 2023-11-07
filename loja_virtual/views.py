from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


def home_page(request):
    context = {
        'title': 'Página Principal',
        'content': 'Bem-vindo a página principal',
    }
    return render(request, 'home_page.html', context)


def about_page(request):
    context = {
        'title': 'Pagina Sobre',
        'content': 'Bem-vindo a página sobre',
    }
    return render(request, 'about/view.html', context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Página de contato',
        'content': 'Bem vindo a página de contato',
        'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    #print(request.POST.get('nome_completo'))
    return render(request, 'contact/view.html', context)