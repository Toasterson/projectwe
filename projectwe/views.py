from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from .models import Project, User


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


class UploadProjectView(LoginRequiredMixin, AccessMixin, generic.CreateView):
    model = Project
    fields = ['picture', 'title', 'idea', 'goal', 'state', 'next_steps', 'preferred_skills']
    template_name_suffix = '_upload_form'

    def form_valid(self, form):
        # Custom Form Post Processing Here
        form.instance.created_by = User.objects.get(user=self.request.user)
        form.instance.members.add(User.objects.get(user=self.request.user))
        return super(UploadProjectView, self).form_valid(form)
