from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Books
from .form import BooksForm

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")

def book_detail_view(request, book_id, *args, **kwargs):
    try:
        obj = Books.objects.get(id=book_id)
        return HttpResponse(f"Kitap Adı: {obj.name} Yazarı: {obj.author}")
    except:
        raise Http404
    
def book_create_view(request, *args, **kwargs):
    form = BooksForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = BooksForm()
        
    return render(request, 'components/form.html', context={'form':form})
