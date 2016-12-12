from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from .models import Project, User as Profile
from registration.backends.simple.views import RegistrationView as BaseRegistrationView
from django.contrib.auth import authenticate, login
from registration import signals
from django.contrib.auth.models import User
from .forms import ProfileEditForm

project_class = Project
project_fields = ['picture', 'title', 'idea', 'goal', 'state', 'next_steps', 'preferred_skills']


# Create your views here.
def index(request):
    return render(request, 'index.html')


def profile(request, username):
    profile_instance = get_object_or_404(Profile.objects, user__username=username)
    return render(request, 'profile.html', {'profile': profile_instance})


class ProfileEditView(LoginRequiredMixin, AccessMixin, generic.FormView):
    template_name = 'profile_edit.html'
    form_class = ProfileEditForm
    success_url = '/user/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates a blank version of the form.
        """
        if self.request.user.username != args[0]:
            return redirect('/')
        profile_instance = Profile.objects.get(user=request.user)
        self.initial = {
            'username': self.request.user.username,
            'firstname': self.request.user.first_name,
            'lastname': self.request.user.last_name,
            'email': self.request.user.email,
            'profile_picture': profile_instance.profile_picture,
            'country': profile_instance.country
        }
        return super(ProfileEditView, self).get(request, args, kwargs)

    def form_valid(self, form):
        self.success_url += self.request.user.username
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        profile_instance = Profile.objects.get(user=self.request.user)
        user = User.objects.get(id=self.request.user.id)
        profile_instance.profile_picture = form.cleaned_data['profile_picture']
        profile_instance.country = form.cleaned_data['country']
        user.first_name = form.cleaned_data['firstname']
        user.last_name = form.cleaned_data['lastname']
        user.email = form.cleaned_data['email']
        profile_instance.save()
        user.save()
        return super(ProfileEditView, self).form_valid(form)


# TODO refactor into signal
class RegistrationView(BaseRegistrationView):
    def register(self, form):
        new_user = form.save()
        new_user = authenticate(
            username=getattr(new_user, User.USERNAME_FIELD),
            password=form.cleaned_data['password1']
        )
        login(self.request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        Profile.objects.create(user=new_user)
        return new_user


class ListView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """Return the Projects."""
        return Project.objects.all()


class DetailView(generic.DetailView):
    model = project_class
    template_name = 'detail.html'


class MembersView(generic.DetailView):
    model = project_class
    template_name = 'members.html'


class UploadProjectView(LoginRequiredMixin, AccessMixin, generic.CreateView):
    model = project_class
    fields = project_fields
    template_name_suffix = '_upload_form'

    def form_valid(self, form):
        # Custom Form Post Processing Here
        user_profile = Profile.objects.get(user=self.request.user)
        form.instance.created_by = user_profile
        return super(UploadProjectView, self).form_valid(form)


class EditProjectView(LoginRequiredMixin, AccessMixin, generic.UpdateView):
    model = project_class
    fields = project_fields
    template_name_suffix = '_edit_form'
