from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

def index(request):

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Number of genres
    num_genres = Genre.objects.count()

    # Number of books with a specific word in title (case-insensitive)
    num_books_with_word = Book.objects.filter(title__icontains='beasts').count()  # Например, 'war'

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,  # ← новая переменная
        'num_books_with_word': num_books_with_word,  # ← новая переменная
    }

    # Render the html template index.html with the data in the context variable
    return render(request, 'index.html', context)

from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

    ''' class Author(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        date_of_birth = models.DateField(null=True, blank=True)
        date_of_death = models.DateField('Died', null=True, blank=True)

        def get_absolute_url(self):
            return reverse('author-detail', args=[str(self.id)])

        def __str__(self):
            return '%s, %s' % (self.last_name, self.first_name)

        class Meta:
            ordering = ['last_name'] 
    '''