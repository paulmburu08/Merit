from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from .forms import ProfileForm,ProjectForm
from .models import Project,Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect(reverse('profile',args=[str(request.user.id)]))

    else:
        form = ProfileForm()

    return render(request, 'new_profile.html',{'form':form})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    try:
        projects = Project.objects.filter(user__id = id)

    except ObjectDoesNotExist:
        raise Http404()

    profile = Profile.get_profile_by_id(id)
    return render(request, 'profile.html',{'profile':profile,'projects':projects})