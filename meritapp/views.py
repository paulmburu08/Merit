from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer
from .forms import ProfileForm,ProjectForm
from .models import Project,Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all().order_by('-create_date')

    return render(request,'index.html',{'projects':projects})

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

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = profile
            post.user = current_user
            post.save()
        return redirect('/')

    else:
        form = ProjectForm()

    return render(request, 'new_project.html',{'form':form})

class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)