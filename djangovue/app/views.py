from django.shortcuts import render

from .models import Album
from .models import Band

# Create your views here.
def frontend(request, slug=None):
    """Vue.js will take care of everything else."""
    bands = Band.objects.all()
    albums = Album.objects.all()

    data = {
        'bands': bands,
        'albums': albums,
    }

    return render(request, 'app/template.html', data)
