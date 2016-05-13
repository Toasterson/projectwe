from django.shortcuts import render
from django.views import generic

from .models import Project


# Create your views here.
def index(request):
    return render(request, 'index.html')


class ListView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """Return the Projects."""
        return Project.objects.all()


class DetailView(generic.DetailView):
    model = Project
    template_name = 'detail.html'
