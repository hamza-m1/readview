from django.shortcuts import render
from .models import About

# Create your views here.


def about(request):
    """
    returns the most recently updated :model: 'about.About' object and 
    displays it in a page.

    **Context**

    ``about``
        A single about object from :model: 'about.About' that is the most 
        recently updated.

    **Template**

    :template:`about/about.html`
    """

    about = About.objects.order_by('-updated_on').first()

    context = {
        'about': about,
    }
    return render(request, 'about/about.html', context)