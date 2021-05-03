from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre
# Funcion-Vista para la pagina de inicio (index())
def index(request):
    #Obtener num de registros.
    num_books=Book.objects.all().count
    num_instances=BookInstance.objects.all().count
    # Registros con filtro
    num_instances_available=BookInstance.objects.filter(status__exact='a').count # Instancias con estatus A
    num_authors=Author.objects.all().count
    num_genre=Genre.objects.all().count
    num_authors_dead= Author.objects.filter(date_of_death__isnull=False).count
    # renderiza el html
    return render(request,'index.html',context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors,'num_genre':num_genre,'num_authors_dead':num_authors_dead})

